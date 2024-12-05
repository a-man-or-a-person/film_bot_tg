# Admin checker

def authentication(func):
    async def wrapper(message):
        if message.from_user.id != 123456789:  # Replace with your Telegram user ID
            return await message.reply("Unauthorized access. Only for administrators.", reply=False)
        return await func(message)
    return wrapper
