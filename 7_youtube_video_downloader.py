# from pytube import YouTube

# link = "https://www.youtube.com/watch?v=YsDyGbToHlI&t=268s"
# youtube_1 = YouTube(link)

# # print(youtube_1.title)
# # print(youtube_1.thumbnail_url)

# videos = youtube_1.streams.all()
# vid=list(enumerate(videos))

# for i in vid:
#     print(i)
# print()
# strm = int(input("Enter: "))
# videos[strm].download()
# print('Succesfully')

# ****Playlist****
from pytube import Playlist

py= Playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9ahPP_vKgaLzfdBV9RutrbWJ")

print(f'Downloading:{py.title}')

for video in py.videos:
    video.streams.first().download()