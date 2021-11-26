from pytube import YouTube
from pytube import Playlist

import os

link = input("Insira o Zelda: ")

yt = Playlist(link)

for url in yt.video_urls:
    ys = YouTube(url)
    print("Titulo = ", ys.title)
    v = ys.streams.get_audio_only()
    out_file = v.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

print("Downloads concluidos!")