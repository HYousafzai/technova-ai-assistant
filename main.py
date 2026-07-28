import os
import uuid
from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing in .env file")


client = genai.Client(api_key=api_key)


app = FastAPI(title="AI Customer Support Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


sessions_db: Dict[str, List[dict]] = {}

SYSTEM_PROMPT = (
    "You are a helpful, courteous, and precise AI Customer Support Specialist "
    "for TechNova Solutions."
)

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    session_id: str

@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    session_id = request.session_id if request.session_id else str(uuid.uuid4())
    user_message = request.message.strip()

    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")

    
    if session_id not in sessions_db:
        sessions_db[session_id] = []

    history = sessions_db[session_id]

    try:
        
        chat = client.chats.create(
            model="gemini-3.6-flash",
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
            ),
            history=history
        )

       
        response = chat.send_message(user_message)
        
        
        sessions_db[session_id] = chat.get_history()

        return ChatResponse(response=response.text, session_id=session_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


app.mount("/", StaticFiles(directory="static", html=True), name="static")