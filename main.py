import os
import shutil
import random

os.mkdir('/home/daniel/Escritorio/Music/')
SOURCE_FOLDER = '/run/media/daniel/HDD/Music/'
DESTINATION_FOLDER = '/home/daniel/Escritorio/Music/'

songs_paths = []
if __name__ == "__main__":
    for artist in os.listdir(SOURCE_FOLDER): 
        for song_path in os.listdir(SOURCE_FOLDER + artist):
            if '.mp3' in song_path:
                songs_paths.append(SOURCE_FOLDER + artist + '/' + song_path)
    random.shuffle(songs_paths)

    for song_path in songs_paths[:300]:
        split_file = song_path.split('/')
        artist = split_file[6]
        song = split_file[7]

        shutil.copyfile(song_path, DESTINATION_FOLDER + artist + '-' + song)