from pyrogram import filters
from pytgcalls.types.input_stream import InputAudioStream
from pytgcalls.types.input_stream.quality import HighQualityAudio
from utils.yt import download
from utils.checks import admin_only

def register(app, call):

    @app.on_message(filters.command(["play", "تشغيل"]))
    @admin_only
    async def play(_, m):
        if len(m.command) < 2:
            return await m.reply("❌ اكتب اسم الأغنية")

        query = " ".join(m.command[1:])
        file = await download(query)

        await call.join_group_call(
            m.chat.id,
            InputAudioStream(file, HighQualityAudio())
        )
        await m.reply(f"🎶 تم التشغيل: **{query}**")