# bert_resume_matcher/app/matcher.py
from sentence_transformers import SentenceTransformer, util

# Load a pre-trained BERT model from Sentence Transformers
model = SentenceTransformer("all-MiniLM-L6-v2")

def compute_similarity_score(resume_text: str, job_description: str) -> float:
    """
    Computes the cosine similarity score between resume and job description text.

    Args:
        resume_text (str): Extracted text from the resume.
        job_description (str): The job description input by the user.

    Returns:
        float: Cosine similarity score between 0 and 1.
    """
    embeddings = model.encode([resume_text, job_description], convert_to_tensor=True)
    similarity = util.pytorch_cos_sim(embeddings[0], embeddings[1])
    return similarity.item()
