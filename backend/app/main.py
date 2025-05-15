from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.chat import generate_response

app = FastAPI(title="Divyastra AI Chatbot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message", "")
    reply = generate_response(user_input)
    return {"response": reply}