import PyPDF2
import re
from typing import Optional


def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts text from a PDF file.

    Args:
        file_path: Path to the PDF file.

    Returns:
        Raw extracted text as a single string. If no text found, returns an empty string.
    """
    text_parts = []

    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        # iterate pages and safely append text (skip None)
        for page in reader.pages:
            page_text: Optional[str] = page.extract_text()
            if page_text:
                text_parts.append(page_text)

    # join with a single space to avoid accidental word merges
    return " ".join(text_parts)


def clean_text(text: str) -> str:
    """
    Removes newlines and collapses multiple spaces from the given text.

    Args:
        text: Raw text to clean.

    Returns:
        A cleaned, single-line string with normalized whitespace.
    """
    if not text:
        return ""

    # Replace newlines with spaces and collapse multiple whitespace into single spaces
    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


if __name__ == "__main__":
    # Minimal test example (commented out - use actual PDF paths for real tests)
    # pdf_path = "path/to/your.pdf"
    # raw = extract_text_from_pdf(pdf_path)
    # print("Raw length:", len(raw))
    # print("Sample:", raw[:400])
    # cleaned = clean_text(raw)
    # print("Cleaned sample:", cleaned[:400])
    pass
