import os
import requests
from pexelsapi.pexels import Pexels


def fetch_pexels_videos(query='nature', count=5, output_dir='tiktoks'):
    api = Pexels(os.getenv("PEXELS_API_KEY"))
    videos = []
    page = 1

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    while len(videos) < count:
        response = api.search_videos(query=query, per_page=count, page=page)
        page += 1
        new_videos = response.get("videos")
        if new_videos:
            videos.extend(new_videos[:count - len(videos)])
        else:
            break

    video_files = []
    for i, video in enumerate(videos):
        video_url = video['video_files'][0]['link']
        video_response = requests.get(video_url)
        if video_response.status_code == 200:
            output_filename = os.path.join(output_dir, f'pexels_video_{i + 1}.mp4')
            with open(output_filename, 'wb') as f:
                f.write(video_response.content)
            print(f"Video {i + 1} background saved as {output_filename}")
            video_files.append(output_filename)
        else:
            print(f"Failed to download video {i + 1}: {video_response.status_code} - {video_response.text}")

    return video_files
