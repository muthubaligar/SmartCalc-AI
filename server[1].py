import os
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from openai import OpenAI

BASE = Path(__file__).parent
app = FastAPI(title="SmartCalc AI")

class SolveRequest(BaseModel):
    question: str = Field(default="", max_length=8000)
    image: str | None = None

@app.get("/api/health")
def health():
    return {"configured": bool(os.getenv("OPENAI_API_KEY"))}

@app.post("/api/solve")
def solve(req: SolveRequest):
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(status_code=503, detail="OPENAI_API_KEY is not configured on the server.")
    if not req.question.strip() and not req.image:
        raise HTTPException(status_code=400, detail="Please enter a question or attach an image.")
    try:
        client = OpenAI()
        prompt = (
            "You are SmartCalc AI, a careful mathematics, physics and engineering tutor. "
            "Explain calculations step by step in clear student-friendly language. "
            "Show formulas, substitutions, units and the final answer. "
            "Check arithmetic and mention assumptions. If the image is unclear, ask for a clearer photo. "
            "Do not pretend to read unreadable text."
        )
        if req.image:
            content = [{"type": "input_text", "text": req.question or "Read and solve the question in this image. Explain step by step."},
                       {"type": "input_image", "image_url": req.image}]
            user_input = [{"role": "user", "content": content}]
        else:
            user_input = req.question
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-5.5"),
            instructions=prompt,
            input=user_input,
            store=False
        )
        return {"answer": response.output_text}
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"AI provider error: {str(exc)[:400]}")

@app.get("/")
def home():
    return FileResponse(BASE / "index.html")

app.mount("/", StaticFiles(directory=BASE), name="static")
