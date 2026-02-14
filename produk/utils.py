import requests
import hashlib
from datetime import datetime
from .models import Produk, Kategori, Status

API_URL = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"


def generate_password(prefix):
    now = datetime.now()
    tanggal = now.strftime("%d")
    bulan = now.strftime("%m")
    tahun = now.strftime("%y")

    raw_password = f"{prefix}-{tanggal}-{bulan}-{tahun}"
    return hashlib.md5(raw_password.encode()).hexdigest()


def get_fastprint_data():

    session = requests.Session()

    # ================================
    # REQUEST PERTAMA (AMBIL HEADER)
    # ================================
    response = session.post(API_URL)

    if response.status_code != 400:
        raise Exception("Gagal mengambil header dari API")

    if not session.cookies.get_dict():
        raise Exception("Cookie tidak ditemukan")

    username_raw = response.headers.get("X-Credentials-Username")
    password_raw = response.headers.get("X-Credentials-Password")

    if not username_raw or not password_raw:
        raise Exception("Header credential tidak ditemukan")

    username_clean = username_raw.split(" ")[0]

    password_after_equal = password_raw.split("=")[1].strip()
    password_prefix = password_after_equal.split("-")[0]

    password_final = generate_password(password_prefix)

    # ================================
    # LOGIN REQUEST
    # ================================
    login = session.post(API_URL, data={
        "username": username_clean,
        "password": password_final
    })

    if login.status_code != 200:
        raise Exception("Login API gagal")

    response_json = login.json()

    if response_json.get("error") != 0:
        raise Exception("API mengembalikan error")

    if "data" not in response_json:
        raise Exception("Data tidak ditemukan di response API")

    produk_list = response_json["data"]

    # ================================
    # SIMPAN KE DATABASE
    # ================================
    for item in produk_list:

        kategori_obj, _ = Kategori.objects.get_or_create(
            nama_kategori=item["kategori"]
        )

        status_obj, _ = Status.objects.get_or_create(
            nama_status=item["status"]
        )

        Produk.objects.update_or_create(
            id_produk=item["id_produk"],
            defaults={
                "nama_produk": item["nama_produk"],
                "harga": int(item["harga"]),
                "kategori": kategori_obj,
                "status": status_obj
            }
        )

    return True
