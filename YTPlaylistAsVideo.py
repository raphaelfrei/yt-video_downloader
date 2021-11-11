from pytube import YouTube
from pytube import Playlist

from pytube.cli import on_progress

link = input("Insira o link: ")

yt = Playlist(link)

for url in yt.video_urls:
    ys = YouTube(url)
    print("Titulo = ", ys.title)
    v = ys.streams.get_highest_resolution()
    v.download()
    print("Baixando...")