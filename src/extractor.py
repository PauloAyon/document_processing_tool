import spacy
import yake

nlp = spacy.load("en_core_web_sm")


def extract_entities(text: str) -> dict:
    """Extract named entities from text using spaCy."""
    doc = nlp(text)
    entities = {}

    for ent in doc.ents:
        if ent.label_ not in entities:
            entities[ent.label_] = []
        if ent.text not in entities[ent.label_]:
            entities[ent.label_].append(ent.text)

    return entities


def extract_keywords(text: str, max_keywords: int = 10) -> list:
    """Extract top keywords from text using YAKE."""
    extractor = yake.KeywordExtractor(
        lan="en",
        n=2,
        top=max_keywords
    )
    keywords = extractor.extract_keywords(text)
    return [kw for kw, score in keywords]