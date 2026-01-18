# NER API for People’s Names & Address

A standalone **Named Entity Recognition (NER) API** built with **FastAPI** and **spaCy** to detect **Personally Identifiable Information (PII)** such as **PERSON** and **ADDRESS** from text.  
This service is designed as an independent backend for AI systems that require PII detection and guardrail enforcement.

---

## ✨ Features

- 🔍 Custom-trained spaCy NER model
- 🧑 Detects PERSON entities
- 🏠 Detects ADDRESS entities
- 🚀 REST API built with FastAPI
- 🔌 Easy integration with external AI agents or guardrail services
- 📦 Lightweight and production-ready

---

## 🏗️ Project Structure

```
API-NER-for-People-s-Names-Address/
├── ner_service/
│   ├── model/              # Trained spaCy NER model
│   ├── dataset/            # Training dataset (JSON)
│   ├── train_ner.py        # Training script
│   └── main.py             # FastAPI application
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Tech Stack

- Python 3.10+
- spaCy
- FastAPI
- Uvicorn

---

## 📦 Installation

### 1. Clone Repository
```bash
git clone https://github.com/cakrasyafiq/API-NER-for-People-s-Names-Address.git
```

Go to project directory
```bash
cd API-NER-for-People-s-Names-Address
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

Activate virtual environment:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API

```bash
uvicorn ner_service.main:app --reload --port 8001
```

API will be available at:
```
http://127.0.0.1:8001
```

Swagger documentation:
```
http://127.0.0.1:8001/docs
```

---

## 📡 API Endpoint

### POST `/ner`

#### Request Body
```json
{
  "text": "Nama saya Budi Santoso dan tinggal di Jalan Sudirman Jakarta"
}
```

#### Response
```json
{
  "entities": [
    {
      "start": 10,
      "end": 22,
      "label": "PERSON"
    },
    {
      "start": 36,
      "end": 59,
      "label": "ADDRESS"
    }
  ]
}
```

**Note:**  
This API returns **only entity metadata** (`start`, `end`, `label`).  
Text masking and redaction are handled by downstream services such as a guardrail or AI agent.

---

## 🧠 Model Training (Optional)

To retrain the NER model:
```bash
python ner_service/train_ner.py
```

Training dataset location:
```
ner_service/dataset/train.json
```

---

## 🔐 Example Use Cases

- AI Customer Service Guardrail
- PII Detection & Compliance
- Input Sanitization for LLM-based Systems

---

## 👤 Author

**Putra Syafiq**  
AI Engineer Internship – Take Home Test Project

---

## 📄 License

This project is intended for educational and evaluation purposes.
