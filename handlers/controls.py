from pyrogram import filters
from utils.checks import admin_only

def register(app, call):

    @app.on_callback_query()
    @admin_only
    async def controls(_, q):
        chat_id = q.message.chat.id

        if q.data == "pause":
            await call.pause_stream(chat_id)
            await q.answer("⏸ تم الإيقاف")

        elif q.data == "play":
            await call.resume_stream(chat_id)
            await q.answer("▶️ تم الاستئناف")

        elif q.data == "stop":
            await call.leave_group_call(chat_id)
            await q.answer("⏹ تم الإنهاء")