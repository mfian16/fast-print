# 🧾 Fast Print — Test Junior Programmer

Aplikasi ini dibuat sebagai solusi untuk **Tes Junior Programmer Fast Print** menggunakan **Django + MySQL + Django REST Framework**.

---

# 🚀 Fitur Utama

✅ Mengambil data produk dari API Fast Print
✅ Validasi login menggunakan header, cookies, dan MD5 password
✅ Menyimpan data ke database MySQL
✅ Menampilkan semua produk
✅ Filter produk **“bisa dijual”**
✅ CRUD produk (Tambah, Edit, Hapus)
✅ Validasi form
✅ Konfirmasi hapus
✅ Pagination & Search
✅ REST API endpoint menggunakan DRF

---

# 🧰 Teknologi yang Digunakan

* Python 3.11.6
* Django
* Django REST Framework
* MySQL (XAMPP 8.2.12)
* Bootstrap 5
* Requests

---

# ⚙️ Cara Menjalankan Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/mfian16/fast-print.git
cd fast-print
```

---

## 2️⃣ Buat Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependency

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Setup Database MySQL

Buat database di phpMyAdmin:

```
fastprint_db
```

Edit `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fastprint_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

---

## 5️⃣ Migrasi Database

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 6️⃣ Import Data dari API

```bash
python manage.py impor_produk
```

---

## 7️⃣ Jalankan Server

```bash
python manage.py runserver
```

Buka browser:

👉 http://127.0.0.1:8000/

---

# 🌐 Endpoint API

| Method | Endpoint                 | Keterangan         |
| ------ | ------------------------ | ------------------ |
| GET    | /api/produk/             | Semua produk       |
| GET    | /api/produk/bisa-dijual/ | Produk bisa dijual |
| GET    | /api/produk/<id>/        | Detail produk      |
| POST   | /api/produk/create/      | Tambah produk      |
| PUT    | /api/produk/update/<id>/ | Update produk      |
| DELETE | /api/produk/delete/<id>/ | Hapus produk       |

---

# 📂 Struktur Project

```
fast_print/
│
├── fast_print/
├── produk/
│   ├── templates/
│   ├── static/
│   ├── management/
│   ├── models.py
│   ├── views.py
│   ├── api_views.py
│   ├── serializers.py
│   ├── forms.py
│   ├── utils.py
│   └── urls.py
│   media/
│   ├── api-filter.png
│   ├── api-list.png
│   ├── Diagram-Database.png
│   ├── ui-filter.png
│   ├── ui-form-edit-produk.png
│   ├── ui-form-tambah-produk.png
│   ├── ui-list.png
├── manage.py
├── requirements.txt
└── README.md

```

---

# 🧠 Catatan Teknis

Aplikasi memanfaatkan:

* Header response untuk mengambil username
* Cookie session dari API
* Password MD5 dinamis berbasis tanggal
* Serializer untuk endpoint API

---

# 🎬 Demo Aplikasi

Video demo dapat dilihat di link berikut:

👉 https://drive.google.com/file/d/1xL1VmWI46y8NqObHB8mVnFrWcLVMnKUh/view

# 👤 Author

Nama: Muhammad Fiqih Irfiansyah
Test Programmer — Fast Print

---
