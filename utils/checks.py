from config import OWNER_ID

def admin_only(func):
    async def wrapper(client, message):
        user = message.from_user.id
        if user == OWNER_ID:
            return await func(client, message)

        member = await client.get_chat_member(message.chat.id, user)
        if member.status not in ["administrator", "creator"]:
            return await message.reply("⛔ للمشرفين فقط")
        return await func(client, message)
    return wrapper