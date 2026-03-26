from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from src.extractor import extract_entities, extract_keywords
import nltk

nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)


def summarize_text(text: str, sentences: int = 3) -> str:
    """Generate an extractive summary using LSA algorithm."""
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences)
    return " ".join(str(sentence) for sentence in summary)


def process_document(text: str, filename: str = "document") -> dict:
    """Run the full NLP pipeline on a text and return structured results."""
    print(f"Processing: {filename}")

    entities = extract_entities(text)
    keywords = extract_keywords(text)
    summary = summarize_text(text)

    return {
        "filename": filename,
        "summary": summary,
        "keywords": keywords,
        "entities": entities,
        "stats": {
            "total_words": len(text.split()),
            "total_entities": sum(len(v) for v in entities.values()),
            "total_keywords": len(keywords)
        }
    }