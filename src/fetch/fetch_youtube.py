import os
from googleapiclient.discovery import build
from pytube import YouTube
from datetime import datetime, timedelta
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips


def fetch_youtube_video(query, api_key, output_dir='tiktoks', min_duration=90, max_duration=180):
    # Build YouTube API client
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Calculate the date 3 days ago
    three_days_ago = (datetime.utcnow() - timedelta(days=3)).strftime('%Y-%m-%dT%H:%M:%SZ')

    # Search for videos in the "medium" duration category (4-20 minutes)
    search_response = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        order='viewCount',
        publishedAfter=three_days_ago,
        videoDuration='medium',
        maxResults=1
    ).execute()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    video_files = []
    for item in search_response['items']:
        video_id = item['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        yt = YouTube(video_url)
        stream = yt.streams.filter(res="720p").first()  # You can adjust resolution
        output_filename = os.path.join(output_dir, 'youtube_video_full.mp4')
        stream.download(output_path=output_dir, filename='youtube_video_full.mp4')
        print(f"Video downloaded as {output_filename}")

        # Trim the video to the desired length
        trimmed_filename = os.path.join(output_dir, 'youtube_video_trimmed.mp4')
        video_duration = yt.length
        if video_duration > max_duration:
            start_time = 0
            end_time = max_duration
        elif video_duration < min_duration:
            print(f"Video is too short ({video_duration} seconds). Skipping.")
            continue
        else:
            start_time = 0
            end_time = video_duration

        ffmpeg_extract_subclip(output_filename, start_time, end_time, targetname=trimmed_filename)

        # Reopen the trimmed video to check audio
        video_clip = VideoFileClip(trimmed_filename)
        if video_clip.audio is None:
            print(f"Warning: No audio found in {trimmed_filename}")
        video_files.append(trimmed_filename)
        print(f"Video trimmed and saved as {trimmed_filename}")

    return video_files

# Example usage:
# api_key = os.getenv('YOUTUBE_API_KEY')
# fetch_youtube_video('news', api_key)
