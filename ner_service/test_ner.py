import spacy
import os

# Load model hasil training
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model")

nlp = spacy.load(MODEL_PATH)

# Text untuk testing
texts = [
    "Nama saya Budi dan tinggal di Jalan Sudirman Jakarta",
    "Perkenalkan Andi Pratama, alamat di Jalan Merdeka Bandung",
    "Saya Siti Aminah rumah di Jalan Diponegoro Surabaya",
    
    # Nama 1 kata
    "Nama saya Bima tinggal di Jalan Merpati Jakarta",
    "Saya Raka alamat di Jalan Anggrek Bandung",

    # Nama 2 kata
    "Perkenalkan Dedi Saputra, rumah di Jalan Kenanga Surabaya",
    "Nama saya Lina Wati tinggal di Jalan Cendana Semarang",

    # Nama 3–4 kata
    "Saya Muhammad Rizky Pratama tinggal di Jalan Ahmad Dahlan Jakarta",
    "Perkenalkan Abdul Rahman Fadillah, alamat di Jalan Veteran Surabaya",
    "Nama saya Bintang Cahaya Putri tinggal di Jalan Pahlawan Malang",

    # Format dibalik
    "Tinggal di Jalan Kartini Semarang, nama saya Taufik Hidayat",
    "Alamat saya di Jalan Gajah Mada Yogyakarta, saya Ayu Lestari",

    # Tanpa kata 'Jalan'
    "Nama saya Rudi tinggal di Sudirman Jakarta",
    "Perkenalkan Sinta, rumah di Diponegoro Malang",

    # Informal
    "Aku Andi tinggal di Jalan Pemuda Bandung",
    "Saya Bayu di Jalan Diponegoro Malang",

    # Negative case (tidak ada entity)
    "Saya ingin menanyakan status pengiriman paket",
    "Bagaimana cara reset password akun saya",
    "Tolong bantu saya dengan masalah pembayaran",
    "Apakah customer service tersedia 24 jam"
]

for text in texts:
    print("=" * 50)
    print("Text:", text)
    doc = nlp(text)
    
    ALLOWED_LABELS = ["PERSON", "ADDRESS"]

    for ent in doc.ents:
        if ent.label_ in ALLOWED_LABELS:
            print(f"{ent.text} -> {ent.label_}")
