from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CommentRequest(BaseModel):
    comment: str


@app.post("/comment")
async def analyze_comment(request: CommentRequest):
    text = request.comment.lower()

    if any(word in text for word in ["terrible", "dreadful", "bad", "broke", "worst"]):
        sentiment = "negative"
        rating = 1

    elif any(word in text for word in ["okay", "average", "functional", "fine"]):
        sentiment = "neutral"
        rating = 3

    else:
        sentiment = "positive"
        rating = 4

    return {
        "sentiment": sentiment,
        "rating": rating
    }