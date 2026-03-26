import os
import sys
from pypdf import PdfReader
from src.processor import process_document
from src.exporter import export_to_json


def read_file(filepath: str) -> str:
    """Read content from TXT or PDF file."""
    if filepath.endswith(".pdf"):
        reader = PdfReader(filepath)
        return " ".join(page.extract_text() for page in reader.pages)
    elif filepath.endswith(".txt"):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    else:
        raise ValueError(f"Unsupported file type: {filepath}")


def process_all(samples_dir: str = "samples"):
    """Process all documents in the samples folder."""
    files = [f for f in os.listdir(samples_dir)
             if f.endswith(".txt") or f.endswith(".pdf")]

    if not files:
        print("No documents found in /samples folder.")
        return

    print(f"Found {len(files)} document(s) to process.\n")

    for filename in files:
        filepath = os.path.join(samples_dir, filename)
        try:
            text = read_file(filepath)
            name = os.path.splitext(filename)[0]
            result = process_document(text, filename=name)
            export_to_json(result)
            print(f"Done: {filename}\n")
        except Exception as e:
            print(f"Error processing {filename}: {e}\n")


if __name__ == "__main__":
    process_all()