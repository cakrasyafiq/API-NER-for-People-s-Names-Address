venv\Scripts\activate

cd ner_service

uvicorn main:app --host 127.0.0.1 --port 8001