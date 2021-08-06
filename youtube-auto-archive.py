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

    download_list = open("/mount/targets.txt", "r").read().splitlines()

    for line in download_list:
        target, destinationfolder, reverse = line.split(",")
        if reverse.lower() in ["true", "y", "yes"]:
            reverse = True
        else:
            reverse = False
        print(f"Downloading {target} to {destinationfolder} in reverse-mode {str(reverse)}")
        youtube_dl_options = {
            "cookiefile": "/mount/cookies.txt",
            "outtmpl": f"/mount/{destinationfolder}/%(playlist_index)s-%(title)s-%(id)s.%(ext)s",
            "writesubtitles": True,
            "allsubtitles": True,
            "writethumbnail": True,
            "writedescription": True,
            "writeannotations": True,
            "ignoreerrors": True,
            "cachedir": False,
            "daterange": daterange,
            "playlistreverse": reverse,
            "postprocessors": [{
                "key": "FFmpegEmbedSubtitle"
            }]
        }

        ytdl = youtube_dl.YoutubeDL(youtube_dl_options)
        ytdl.download([target])
    
    print(f"Now sleeping for {environ['SLEEPMIN']} minutes")
    sleep(sleeptime)

