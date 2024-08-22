from pytube import YouTube

link = input('Please enter the link : ')
yt = YouTube(link)
print("Title : ", yt.title)
print("View : ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download("YouTube video download/result")
