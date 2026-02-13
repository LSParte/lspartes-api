from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
from vision_module import analyze_image
from recommendation_module import generate_recommendations

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "LSPartes API Online 🚀"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    contents = await file.read()
    vision_result = analyze_image(contents)
    recommendations = generate_recommendations(vision_result)
    return {
        "analysis": vision_result,
        "recommendations": recommendations
    }
