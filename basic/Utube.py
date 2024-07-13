from pytube import YouTube

# URL of the YouTube video
url = 'https://youtu.be/HkW9hH2JBz0?si=gqlh3Y_3yznGZVfZ'

# Create a YouTube object
yt = YouTube(url)

# Get the video stream with 720p resolution
video_stream = yt.streams.filter(res="720p", file_extension='mp4').first()

# Check if the video stream is available
if video_stream:
    # Download the video
    video_stream.download(output_path='Downloads', filename='video.mp4')
    print("Download completed!")
else:
    print("720p resolution not available for this video.")
