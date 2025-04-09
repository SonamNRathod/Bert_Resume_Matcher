# bert_resume_matcher/app/main.py
import os
from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import JSONResponse
from app.matcher import compute_similarity_score
from app.parser import extract_text_from_pdf

app = FastAPI()

@app.post("/match")
async def match_resume(
    resume_file: UploadFile,
    job_description: str = Form(...)
):
    content = await resume_file.read()
    resume_text = extract_text_from_pdf(content)
    score = compute_similarity_score(resume_text, job_description)
    return JSONResponse({"similarity_score": round(score * 100, 2)})

# Streamlit Frontend (optional, can be separated into a different file)
import streamlit as st
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000/match")

st.title("Resume vs Job Description Matcher")

uploaded_file = st.file_uploader("Upload your Resume (PDF)")
job_text = st.text_area("Paste the Job Description")

if uploaded_file and job_text:
    with st.spinner("Calculating match score..."):
        files = {"resume_file": uploaded_file}
        data = {"job_description": job_text}
        response = requests.post(API_URL, files=files, data=data)
        if response.status_code == 200:
            st.success(f"Match Score: {response.json()['similarity_score']}%")
        else:
            st.error("Something went wrong.")
