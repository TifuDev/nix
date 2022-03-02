from src.feedbot import app

if __name__ == "__main__":
    try:
        app.run(print("Bot started!"))
    except ConnectionError as err:
        print(err)
        exit(1)
