import os
from dotenv import load_dotenv
from groq import AsyncGroq
from typing import List, Dict,Any
load_dotenv()
import asyncio

async def make_llm_call(prompt:str):
    client=AsyncGroq(api_key=os.environ['GROQ_API_KEY'])
    messages=[{
        "role":"user",
        "content":prompt
    }]
    chat_completion=await client.chat.completions.create(messages=messages,model="llama-3.3-70b-versatile", temperature=0.5, max_completion_tokens=1024,top_p=1,stream=True,stop=None
)
    sinopsis=""
    async for chunk in chat_completion:
        if chunk.choices[0].delta.content is not None:
            sinopsis+=chunk.choices[0].delta.content+" "
    return sinopsis

async def make_visual_llm_call(messages:List[Dict[str,Any]]):
    client = AsyncGroq(api_key=os.environ.get("GROQ_API_KEY"))
        
    completion =await  client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    result=""
    async for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            result+=chunk.choices[0].delta.content+" "
    return result