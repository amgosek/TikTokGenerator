import boto3
import os


def text_to_speech(text, voice, output_filename='output.mp3'):
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    aws_region = os.getenv('AWS_REGION')

    polly_client = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=aws_region
    ).client('polly')

    response = polly_client.synthesize_speech(
        VoiceId=voice,
        OutputFormat='mp3',
        Text=text
    )

    with open(output_filename, 'wb') as f:
        f.write(response['AudioStream'].read())

    return output_filename
