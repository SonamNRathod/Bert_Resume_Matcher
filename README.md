# BERT-Powered Resume Ranker + Job Matcher

This project helps evaluate how well a resume matches a job description using semantic similarity powered by BERT embeddings.

---

## Features
- Upload a resume (PDF)
- Paste any job description
- Get a **match score (%)** based on BERT similarity
- Interactive frontend using Streamlit
- RESTful API using FastAPI
- Configurable API endpoint via environment variable (`API_URL`)

---

## Tech Stack
- **NLP Model**: Sentence Transformers (`all-MiniLM-L6-v2`)
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **PDF Parsing**: PyMuPDF (`fitz`)

---

## Project Structure
```
bert_resume_matcher/
├── app/
│   ├── main.py            # FastAPI backend + Streamlit frontend
│   ├── matcher.py         # BERT-based similarity computation
│   ├── parser.py          # PDF text extractor
│   ├── utils.py           # (optional) Logger or helpers
│   └── __init__.py        # Makes `app` a package
├── tests/                 # (optional) Unit tests
├── requirements.txt       # Project dependencies
└── README.md              # You're here!
```

---

## Setup & Run
### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/bert_resume_matcher.git
cd bert_resume_matcher
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Server
```bash
uvicorn app.main:app --reload
```
Access API at: `http://localhost:8000/docs`

### 4. Run Streamlit App
In a **separate terminal**:
```bash
streamlit run app/main.py
```

---

## 💡 Inspiration
Built to bridge the gap between machine learning and real-world job matching use cases. Ideal for job seekers, recruiters, and career platforms.

---
