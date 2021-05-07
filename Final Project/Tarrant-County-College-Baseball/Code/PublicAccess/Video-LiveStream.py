# Reference 1: https://video.aminyazdanpanah.com/python/start?r=hls
# Reference 2: https://github.com/gwgowdey/Tarrant-County-College-Baseball/blob/main/Documentation/FFmpeg%20Basics%20Guide%20Book.pdf
# Video angles diagram: https://github.com/gwgowdey/Tarrant-County-College-Baseball/tree/main/Images/7.jpg

# pip install ffmpeg-python-video-streaming

# IP cameras with regular speed video are connected via ethernet to a switch. User connects their computer to the switch.
# Video angles stream to the website.

# Not functional - just a proof of concept.

import ffmpeg_streaming

print("Main/Center Field (A)")
video = ffmpeg_streaming.input('Local IP address of Main/Center Field (A)', capture = True)

print("Behind Home Plate/Field (E)")
video = ffmpeg_streaming.input('Local IP address of Behind Home Plate/Field (E)', capture = True)

print("Open LHP (G)") 
video = ffmpeg_streaming.input(' Local IP address of Open LHP (G)', capture = True)

print("Open RHH (H)")
video = ffmpeg_streaming.input('Local IP address of Open RHH (H)', capture = True)

print("Open RHP (I)")
video = ffmpeg_streaming.input('Local IP address of Open RHP (I)', capture = True)

print("Open LHH (J)")
video = ffmpeg_streaming.input('Local IP address of Open LHH (J)', capture = True)