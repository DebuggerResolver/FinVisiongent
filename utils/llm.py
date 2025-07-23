import os
from dotenv import load_dotenv
from groq import Groq
from typing import List, Dict,Any
load_dotenv()

def make_llm_call(prompt:str):
    client=Groq(api_key=os.environ['GROQ_API_KEY'])
    messages=[{
        "role":"user",
        "content":prompt
    }]
    chat_completion=client.chat.completions.create(messages=messages,model="llama-3.3-70b-versatile")
    sinopis=chat_completion.choices[0].message.content
    return sinopis

def make_visual_llm_call(messages:List[Dict[str,Any]]):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=messages,
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )

    result=completion.choices[0].message.content
    return result