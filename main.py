from pytubefix import YouTube
import os


with open("in.txt", "r") as file:
    lines = []
    for line in file:
        line = line.strip()
        lines.append(line)


for r in lines:
    yt = YouTube(r)

    stream = yt.streams.filter(only_audio=True).first()
    output_file = stream.download(output_path="./out")

    base, ext = os.path.splitext(output_file)
    new_file = base + ".mp3"

    os.rename(output_file, new_file)

    print(f"{yt.title} has been downlaoded!")
    


