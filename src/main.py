import os
import sys
from dotenv import load_dotenv
from fetch.fetch_facts import fetch_fun_facts
from fetch.fetch_trivia import fetch_trivia_facts
from fetch.fetch_wikipedia_facts import fetch_wikipedia_facts
from fetch.fetch_video import fetch_pexels_videos
from fetch.fetch_youtube import fetch_youtube_video
from utils.text_to_speech import text_to_speech
from utils.create_video import create_video_with_audio, create_youtube_video

# Load environment variables from .env file
load_dotenv()

# Set environment variable to disable parallelism for tokenizers
os.environ["TOKENIZERS_PARALLELISM"] = "false"


def get_user_choice():
    while True:
        choice = input("Choose type of TikTok (facts/wiki/trivia/youtube): ").strip().lower()
        if choice in ['facts', 'wiki', 'trivia', 'youtube']:
            return choice
        else:
            print("Invalid choice. Please enter 'facts', 'wiki', 'trivia', or 'youtube'.")


# Add src directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Ensure the tiktoks directory exists
base_dir = os.path.dirname(os.path.abspath(__file__))
tiktoks_dir = os.path.join(base_dir, 'tiktoks')
os.makedirs(tiktoks_dir, exist_ok=True)

# Get user's choice for the type of TikTok
choice = get_user_choice()

if choice == 'wiki':
    # Subject for the facts
    subject = input("Enter the Wikipedia subject: ").strip().replace(" ", "_")
    facts = fetch_wikipedia_facts(subject, 5)
    fact_count = len(facts)
    intro_text = f"Here are {fact_count} things that have happened on {subject.replace('_', ' ')}"
    video_query = subject.replace('_', ' ')

    # Convert facts to audio files
    audio_files = []

    # Add introduction
    audio_file = os.path.join(tiktoks_dir, 'intro.mp3')
    text_to_speech(intro_text, audio_file)
    audio_files.append(audio_file)

    # Add numbered facts
    for i, fact in enumerate(facts):
        numbered_fact = f"Number {i+1}. {fact}"
        audio_file = os.path.join(tiktoks_dir, f'fact_{i+1}.mp3')
        text_to_speech(numbered_fact, audio_file)
        audio_files.append(audio_file)

    # Add closing message
    closing_text = "Thanks for watching, like and follow for more!"
    closing_audio_file = os.path.join(tiktoks_dir, 'closing.mp3')
    text_to_speech(closing_text, closing_audio_file)
    audio_files.append(closing_audio_file)

    # Fetch multiple Pexels videos with the relevant query
    pexels_videos = fetch_pexels_videos(query=video_query, output_dir=tiktoks_dir)

    # Ensure we have enough videos to match the number of facts plus the intro and closing
    if len(pexels_videos) < len(audio_files):
        pexels_videos = pexels_videos * (len(audio_files) // len(pexels_videos) + 1)

    # Generate final video filename
    output_filename = os.path.join(tiktoks_dir, 'final_video.mp4')

    # Create video with background and audio
    create_video_with_audio(pexels_videos[:len(audio_files)], audio_files, output_filename)

    # Cleanup temporary audio files
    for audio_file in audio_files:
        os.remove(audio_file)

elif choice == 'facts':
    facts = fetch_fun_facts(5)
    fact_count = len(facts)
    intro_text = f"Here are {fact_count} fun facts you didn't know"
    video_query = input("Enter a query word for the background videos: ").strip()

    # Convert facts to audio files
    audio_files = []

    # Add introduction
    audio_file = os.path.join(tiktoks_dir, 'intro.mp3')
    text_to_speech(intro_text, audio_file)
    audio_files.append(audio_file)

    # Add numbered facts
    for i, fact in enumerate(facts):
        numbered_fact = f"Number {i+1}. {fact}"
        audio_file = os.path.join(tiktoks_dir, f'fact_{i+1}.mp3')
        text_to_speech(numbered_fact, audio_file)
        audio_files.append(audio_file)

    # Add closing message
    closing_text = "Thanks for watching!"
    closing_audio_file = os.path.join(tiktoks_dir, 'closing.mp3')
    text_to_speech(closing_text, closing_audio_file)
    audio_files.append(closing_audio_file)

    # Fetch multiple Pexels videos with the relevant query
    pexels_videos = fetch_pexels_videos(query=video_query, output_dir=tiktoks_dir)

    # Ensure we have enough videos to match the number of facts plus the intro and closing
    if len(pexels_videos) < len(audio_files):
        pexels_videos = pexels_videos * (len(audio_files) // len(pexels_videos) + 1)

    # Generate final video filename
    output_filename = os.path.join(tiktoks_dir, 'final_video.mp4')

    # Create video with background and audio
    create_video_with_audio(pexels_videos[:len(audio_files)], audio_files, output_filename)

    # Cleanup temporary audio files
    for audio_file in audio_files:
        os.remove(audio_file)

elif choice == 'trivia':
    facts = fetch_trivia_facts(5)
    fact_count = len(facts)
    intro_text = f"Here are {fact_count} trivia facts you didn't know"
    video_query = input("Enter a query word for the background videos: ").strip()

    # Convert facts to audio files
    audio_files = []

    # Add introduction
    audio_file = os.path.join(tiktoks_dir, 'intro.mp3')
    text_to_speech(intro_text, audio_file)
    audio_files.append(audio_file)

    # Add numbered facts
    for i, fact in enumerate(facts):
        numbered_fact = f"Number {i+1}. {fact}"
        audio_file = os.path.join(tiktoks_dir, f'fact_{i+1}.mp3')
        text_to_speech(numbered_fact, audio_file)
        audio_files.append(audio_file)

    # Add closing message
    closing_text = "Thanks for watching!"
    closing_audio_file = os.path.join(tiktoks_dir, 'closing.mp3')
    text_to_speech(closing_text, closing_audio_file)
    audio_files.append(closing_audio_file)

    # Fetch multiple Pexels videos with the relevant query
    pexels_videos = fetch_pexels_videos(query=video_query, output_dir=tiktoks_dir)

    # Ensure we have enough videos to match the number of facts plus the intro and closing
    if len(pexels_videos) < len(audio_files):
        pexels_videos = pexels_videos * (len(audio_files) // len(pexels_videos) + 1)

    # Generate final video filename
    output_filename = os.path.join(tiktoks_dir, 'final_video.mp4')

    # Create video with background and audio
    create_video_with_audio(pexels_videos[:len(audio_files)], audio_files, output_filename)

    # Cleanup temporary audio files
    for audio_file in audio_files:
        os.remove(audio_file)

elif choice == 'youtube':
    video_query = input("Enter a query word for YouTube videos: ").strip()
    api_key = os.getenv('YOUTUBE_API_KEY')

    # Fetch YouTube video based on the query
    youtube_videos = fetch_youtube_video(query=video_query, api_key=api_key, output_dir=tiktoks_dir)

    # Generate final video filename
    output_filename = os.path.join(tiktoks_dir, 'final_video.mp4')

    # Create video with YouTube background and YouTube audio
    create_youtube_video(youtube_videos, output_filename)
