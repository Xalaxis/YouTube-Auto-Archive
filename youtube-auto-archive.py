import youtube_dl
from datetime import datetime
from os import environ
from time import sleep
from youtube_dl import DateRange

sleeptime = int(environ["SLEEPMIN"]) * 60

daterange = DateRange(end="today-1day")

# def my_hook(d):
#     if d['status'] == 'finished':
#         print(f"Done downloading {d.filename}")
print("------")
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
        "daterange": daterange,
        "postprocessors": [{
            "key": "FFmpegEmbedSubtitle"
        }]
    }

    with youtube_dl.YoutubeDL(youtube_dl_options) as ytdl:
        ytdl.download([environ["TODOWNLOAD"]])
    
    print(f"Now sleeping for {environ['SLEEPMIN']} minutes")
    sleep(sleeptime)

