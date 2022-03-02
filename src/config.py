"""
Set up environment to start bot
"""

from datetime import datetime
from pathlib import Path

import logging
import os

import yaml

date = datetime.now().replace(microsecond=0).isoformat()

logfile = Path(f"logs/{date}.log")
configfile = Path("config.yaml")

if not logfile.parent.exists():
    logfile.parent.mkdir()

logging.basicConfig(filename=logfile, encoding="utf-8", level=logging.DEBUG)

config = {
    "message": {
        "template": "**{title}**\n\n" "__{description}__\n\n" "[{channel_name}]({url})"
    },
    "channels": [
        "https://sputniknews.com/export/rss2/archive/index.xml",
    ],
}

if not configfile.exists():
    configfile.write_text(yaml.dump(config), encoding="utf-8")

try:
    SESSION_NAME = os.environ["SESSION_NAME"]
    API_ID = int(os.environ["API_ID"])
    API_HASH = os.environ["API_HASH"]
    TOKEN = os.environ["TOKEN"]

    with open(configfile, "r", encoding="utf-8") as stream:
        config = yaml.safe_load(stream)

except KeyError as err:
    logging.critical("%s environment variable not defined!", err)
except yaml.YAMLError as err:
    logging.critical(err)
