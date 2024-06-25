import os
from moviepy.editor import VideoFileClip, concatenate_audioclips, AudioFileClip, concatenate_videoclips
from src.fetch.fetch_video import fetch_pexels_videos
from PIL import Image


# Ensure compatibility by replacing ANTIALIAS with LANCZOS
Image.ANTIALIAS = Image.LANCZOS


def create_video_with_audio(video_files, audio_files, output_file):
    # Load video clips and resize them
    video_clips = []
    for i, video_file in enumerate(video_files):
        video_clip = VideoFileClip(video_file)

        # Crop video to 9:16 aspect ratio
        video_width, video_height = video_clip.size
        target_aspect_ratio = 9 / 16
        target_width = video_width
        target_height = int(video_width / target_aspect_ratio)

        if target_height > video_height:
            target_height = video_height
            target_width = int(video_height * target_aspect_ratio)

        video_clip = video_clip.crop(width=target_width, height=target_height, x_center=video_width / 2,
                                     y_center=video_height / 2)

        # Resize the video to 1080x1920 for TikTok
        video_clip = video_clip.resize(newsize=(1080, 1920))

        # Get corresponding audio file and its duration
        audio_clip = AudioFileClip(audio_files[i])
        audio_duration = audio_clip.duration

        # Trim the video to match the audio length
        video_clip = video_clip.subclip(0, audio_duration)

        # Set the audio to the video clip
        video_clip = video_clip.set_audio(audio_clip)

        video_clips.append(video_clip)

    # Concatenate video clips
    final_video_clip = concatenate_videoclips(video_clips, method="compose")

    # Write the final video file
    final_video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
    print(f"Video file saved as {output_file}")


def create_youtube_video(video_files, output_file):
    # Load the YouTube video clip
    video_clip = VideoFileClip(video_files[0])

    # Resize the video to 1080x1920 for TikTok
    video_clip = video_clip.resize(newsize=(1080, 1920))

    # Write the final video file
    video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
    print(f"Video file saved as {output_file}")
