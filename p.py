# ... שאר הקוד נשאר בדיוק אותו דבר ...

if __name__ == "__main__":
    # אנחנו מושכים את הטוקן מהגדרות המערכת של Render ולא כותבים אותו בקוד
    token = os.environ.get('DISCORD_TOKEN')
    if not token:
        print("Error: DISCORD_TOKEN not found in environment variables.")
    else:
        bot.run(token)
