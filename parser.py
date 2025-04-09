# bert_resume_matcher/app/parser.py
import fitz 
from typing import Union

def extract_text_from_pdf(pdf_bytes: Union[bytes, bytearray]) -> str:
    """
    Extracts text from a PDF byte stream.

    Args:
        pdf_bytes (bytes): The PDF file content as bytes.

    Returns:
        str: Extracted text from the PDF.
    """
    text = ""
    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()
