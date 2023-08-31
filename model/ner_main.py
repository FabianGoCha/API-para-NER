import spacy

# Creación del modelo para la extracción de entidades nombradas

nlp = spacy.load("es_core_news_sm")


def ner_spacy(text):
    doc1 = nlp(text)
    for ent in doc1.ents:
        yield ent.text, ent.label_
    