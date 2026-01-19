import spacy
from spacy.training.example import Example
import random
import json
import os
from pathlib import Path

# LOAD DATASET (SAFE PATH)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "..", "dataset", "train.json")

with open(DATASET_PATH, "r", encoding="utf-8") as f:
    raw_data = json.load(f)

TRAIN_DATA = []
for item in raw_data:
    TRAIN_DATA.append((item["text"], {"entities": item["entities"]}))
    

# LOAD BASE MODEL
nlp = spacy.load("en_core_web_sm")


# ADD NER LABELS
ner = nlp.get_pipe("ner")
ner.add_label("PERSON")
ner.add_label("ADDRESS")


# TRAINING
optimizer = nlp.resume_training()
EPOCHS = 25

# Disable other pipes to avoid interference
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]
with nlp.disable_pipes(*other_pipes):
    optimizer = nlp.resume_training()

    for epoch in range(EPOCHS):
        random.shuffle(TRAIN_DATA)
        losses = {}

        for text, annotations in TRAIN_DATA:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, annotations)
            nlp.update([example], sgd=optimizer, losses=losses)

        print(f"Epoch {epoch+1}/{EPOCHS} - Loss: {losses}")


# SAVE MODEL
output_dir = Path("model")
output_dir.mkdir(exist_ok=True)
nlp.to_disk(output_dir)

print("✅ Model NER berhasil ditraining dan disimpan di folder 'model/'")
