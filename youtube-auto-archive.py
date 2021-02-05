import youtube_dl
from datetime import datetime
from os import environ
from time import sleep

# def my_hook(d):
#     if d['status'] == 'finished':
#         print(f"Done downloading {d.filename}")

print(f"YouTube Auto Archive starting at {datetime.now()}")

while True:
    print(f"Starting download run at {datetime.now()}")
    youtube_dl_options = {
        "cookiefile": "/output/cookies.txt",
        "outtmpl": "/output/%(title)s-%(id)s.%(ext)s",
        "download_archive": "/output/downloaded.txt",
        "writesubtitles": True,
        "allsubtitles": True,
        "writethumbnail": True,
        "writedescription": True,
        "writeannotations": True,
        "ignoreerrors": True,
        "cachedir": False,
        "postprocessors": [{
            "key": "FFmpegEmbedSubtitle"
        }]
    }

    with youtube_dl.YoutubeDL(youtube_dl_options) as ytdl:
        ytdl.download([environ["TODOWNLOAD"]])
    
    sleep(int(environ["SLEEPMIN"]) * 60)

