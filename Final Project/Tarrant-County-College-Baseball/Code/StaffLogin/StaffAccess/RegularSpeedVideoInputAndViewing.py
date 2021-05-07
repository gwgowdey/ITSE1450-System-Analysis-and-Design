# Reference 1: https://video.aminyazdanpanah.com/python/start?r=hls
# Reference 2: https://github.com/gwgowdey/Tarrant-County-College-Baseball/blob/main/Documentation/FFmpeg%20Basics%20Guide%20Book.pdf
# Video angles diagram: https://github.com/gwgowdey/Tarrant-County-College-Baseball/tree/main/Images/7.jpg

# pip install ffmpeg-python-video-streaming

# Included here would be a selection to access the Private Video Player for viewing purposes and an input section to capture video.
# IP cameras with regular speed video are connected via ethernet to a switch. User connects their computer to the switch.
# Video clips are cut and tagged/labeled with each trigger/input from either TrackMan or Hawk-Eye using their respective API.
# Full game is uploaded to website and high-speed video clips are merged to regular speed video clips through a network folder.

# Not functional - just a proof of concept.

import ffmpeg_streaming

print("Main/Center Field (A)")
video = ffmpeg_streaming.input('Local IP address of Main/Center Field (A)', capture = True)

print("1B Line (B)")
video = ffmpeg_streaming.input('Local IP address of 1B Line (B)', capture = True)

print("3B Line (C)")
video = ffmpeg_streaming.input('Local IP address of 3B Line (C)', capture = True)

print("Overhead/High Home Plate (D)")
video = ffmpeg_streaming.input('Overhead/High Home Plate (D)', capture = True)

print("Behind Home Plate/Field (E)")
video = ffmpeg_streaming.input('Local IP address of Behind Home Plate/Field (E)', capture = True)

print("Home Plate (F)")
video = ffmpeg_streaming.input('Home Plate (F)', capture = True)

print("Open LHP (G)") 
video = ffmpeg_streaming.input(' Local IP address of Open LHP (G)', capture = True)

print("Open RHH (H)")
video = ffmpeg_streaming.input('Local IP address of Open RHH (H)', capture = True)

print("Open RHP (I)")
video = ffmpeg_streaming.input('Local IP address of Open RHP (I)', capture = True)

print("Open LHH (J)")
video = ffmpeg_streaming.input('Local IP address of Open LHH (J)', capture = True)