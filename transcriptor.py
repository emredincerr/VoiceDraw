from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

my_key_openai = os.getenv("openai_apikey")

client = OpenAI(api_key=my_key_openai)

def transcribe_with_whisper(audio_file_name):
    
    audio_file = open(audio_file_name, "rb")
    
    AI_Response = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file,
        language="tr")
    
    return AI_Response.text