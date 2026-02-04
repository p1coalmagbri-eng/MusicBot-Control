from pyrogram import filters, types

def register(app, call):

    @app.on_message(filters.command(["panel", "لوحة"]))
    async def panel(_, m):
        kb = types.InlineKeyboardMarkup([
            [
                types.InlineKeyboardButton("▶️ تشغيل", callback_data="play"),
                types.InlineKeyboardButton("⏸ إيقاف", callback_data="pause")
            ],
            [
                types.InlineKeyboardButton("⏭ تخطي", callback_data="skip"),
                types.InlineKeyboardButton("⏹ إنهاء", callback_data="stop")
            ]
        ])
        await m.reply("🎛 لوحة التحكم بالميوزك", reply_markup=kb)