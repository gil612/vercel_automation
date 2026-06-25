from fastapi import FastAPI
from pydantic import BaseModel
import os
from dotenv import load_dotenv


app = FastAPI()

class TextInput(BaseModel):
    text: str


load_dotenv() # To load variables locally for testing

SECRET_KEY = os.getenv("SECRET_KEY", "Default-Secret")

@app.get("/")
def read_root():
    return {"message": f"ההודעה הסודית היא: {SECRET_KEY}"}

@app.post("/analyze")
def analyze_sentiment(input: TextInput):
    # In a real app, you would use a model here.
    # For this exercise, we'll use a simple rule.
    if "מעולה" in input.text or "מצוין" in input.text:
        sentiment = "positive"
    elif "גרוע" in input.text or "אכזבה" in input.text:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    return {"original_text": input.text, "sentiment": sentiment}