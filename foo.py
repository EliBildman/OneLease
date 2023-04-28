import io
import time
import picamera
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Set the video duration (in seconds)
duration = 10

# Set the output file name
output_file = "my_video.mp4"

# Start recording the video
stream = io.BytesIO()
with picamera.PiCamera() as camera:
    camera.start_recording(stream, format='h264')
    camera.wait_recording(duration)
    camera.stop_recording()

# Convert the output to MP4 format
stream.seek(0)
ffmpeg_extract_subclip(stream, 0, duration, output_file)

# Print the file size
print(f"File size: {os.path.getsize(output_file)} bytes")
