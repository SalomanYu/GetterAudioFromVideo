import sys, time
from moviepy.editor import *

try:
    video = VideoFileClip(sys.argv[1])
    audio = video.audio
    audio.write_audiofile(sys.argv[2])
    print(f'[SUCCESS] The conversion was successful. Result file: {sys.argv[2]}')
except BaseException as error:
    if 'could not be found' in str(error):
        print('[ERROR] File not found\n[TRY] python3 converter.py "/home/user/videoname.mp4" "audioname.mp3" ')
        time.sleep(1)
    elif 'list index out of range' == str(error):
        print('[ERROR] Invalid file name for audio\n[TRY] python3 converter.py "/home/user/videoname.mp4" "audioname.mp3" ')
        time.sleep(1)
    else:
        print(error)
