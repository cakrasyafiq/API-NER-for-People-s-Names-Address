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

## 🏗️ Project Architecture

```
Client / Service Lain
        |
        |  HTTP POST /ner
        |  { "text": "<input text>" }
        v
+----------------------------+
|        FastAPI App         |
|        (NER Service)       |
+----------------------------+
        |
        |  spaCy pipeline
        v
+----------------------------+
|   Custom spaCy NER Model   |
|  (PERSON, ADDRESS)         |
+----------------------------+
        |
        |  Extract entity metadata
        v
+----------------------------+
|  Structured JSON Response |
|  start, end, label        |
+----------------------------+
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

## 🧠 Model Training Pipeline

```
JSON Dataset
   ↓
Format Conversion (spaCy)
   ↓
Load Pretrained Model
   ↓
Add Custom Entity Labels
   ↓
Disable Other Pipelines
   ↓
NER Training Loop
   ↓
Model Saved to Disk
```

---

## 🔐 Try It Out

```bash
Nama saya Budi Santoso dan saya tinggal di Jalan Sudirman Jakarta.
```
→ PERSON, ADDRESS

```bash
Perkenalkan Andi Wijaya, alamat rumah di Jalan Merdeka Bandung.
```
→ PERSON, ADDRESS

```bash
Saya Rina Marlina sekarang menetap di Jalan Diponegoro Surabaya.
```
→ PERSON, ADDRESS

```bash
Nama lengkap Dimas Pratama Putra dan tinggal di Jalan Ahmad Yani Semarang.
```
→ PERSON (3 kata), ADDRESS

```bash
Perkenalkan Taufik Hidayat, saya tinggal di Jalan Gatot Subroto Denpasar.
```
→ PERSON, ADDRESS

```bash
Saya Ayu dan alamat rumah saya di Jalan Asia Afrika Bandung.
```
→ PERSON (1 kata), ADDRESS

```bash
Nama saya Muhammad Rizky Ramadhan Putra dan tinggal di Jalan Pemuda Jakarta.
```
→ PERSON (4 kata), ADDRESS

```bash
Perkenalkan Bayu Prakoso yang saat ini berada di Jalan Pahlawan Malang.
```
→ PERSON, ADDRESS

```bash
Halo, saya ingin menanyakan status pengiriman pesanan saya.
```
→ ❌ No entity expected

```bash
Apakah customer service tersedia 24 jam setiap hari?
```
→ ❌ No entity expected

---

## 👤 Author

**Putra Syafiq**  
AI Engineer Internship – Take Home Test Project

---

## 📄 License

This project is intended for educational and evaluation purposes.
