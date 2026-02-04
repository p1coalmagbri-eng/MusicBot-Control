import yt_dlp

async def download(query):
    ydl_opts = {
        "format": "bestaudio",
        "outtmpl": "cache/%(id)s.%(ext)s",
        "quiet": True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(f"ytsearch:{query}", download=True)
        return ydl.prepare_filename(info["entries"][0])