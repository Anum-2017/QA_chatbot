import os  
import chainlit as cl 
import google.generativeai as genai  
from dotenv import load_dotenv  
import asyncio
from concurrent.futures import ThreadPoolExecutor

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

genai.configure(api_key=gemini_api_key)

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

executor = ThreadPoolExecutor()

def sync_generate(prompt):
    return model.generate_content(prompt)

@cl.on_chat_start
async def handle_chat_start():
    await cl.Message(content="Hello! How can I help you today?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    prompt = message.content
    try:
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(executor, sync_generate, prompt)
        response_text = response.text if hasattr(response, "text") else "Sorry, I couldn't generate a response."
    except Exception as e:
        response_text = f"Error: {str(e)}"
    
    await cl.Message(content=response_text).send()
