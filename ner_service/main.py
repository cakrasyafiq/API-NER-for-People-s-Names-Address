from fastapi import FastAPI
from pydantic import BaseModel
import spacy
import os

# ========== Load Model ==========
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model")

nlp = spacy.load(MODEL_PATH)

# ========== FastAPI App ==========
app = FastAPI(
    title="NER Service",
    description="Custom NER service that extracts PII entities",
    version="1.0"
)

# ========== Request Schema ==========
class NERRequest(BaseModel):
    text: str

# ========== Response Schema ==========
class Entity(BaseModel):
    start: int
    end: int
    label: str

class NERResponse(BaseModel):
    entities: list[Entity]

# ========== Endpoint ==========
@app.post("/ner", response_model=NERResponse)
def extract_entities(request: NERRequest):
    doc = nlp(request.text)

    entities = []
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ADDRESS"]:
            entities.append({
                "start": ent.start_char,
                "end": ent.end_char,
                "label": ent.label_
            })

    return {"entities": entities}