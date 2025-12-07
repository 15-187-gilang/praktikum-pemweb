<img width="1071" height="856" alt="Screenshot 2025-12-07 215516" src="https://github.com/user-attachments/assets/82f8e12f-854c-477c-bc1e-bb95d33824d8" />
# Aplikasi Manajemen Matakuliah dengan Pyramid

Aplikasi API sederhana untuk manajemen matakuliah berdasarkan apa yang telah dipelajari dalam praktikum.
Aplikasi ini adalah API backend untuk mengelola data matakuliah menggunakan Pyramid Framework. Aplikasi menyediakan endpoint REST API untuk operasi CRUD (Create, Read, Update, Delete) pada data matakuliah.



## Cara Instalasi

### 1. Langkah membuat virtual environment

```bash
# Buat virtual environment
python -m venv venv

# Aktivasi virtual environment
# Windows PowerShell:
.\venv\Scripts\Activate.ps1

# Windows CMD:
.\venv\Scripts\activate.bat

# Linux/Mac:
source venv/bin/activate
```

### 2. Instalasi dependensi

```bash
cd pyramid_mahasiswa
pip install -e .
```

### 3. Konfigurasi database

Database sudah dikonfigurasi menggunakan SQLite di file `development.ini`:

```ini
sqlalchemy.url = sqlite:///%(here)s/pyramid_mahasiswa.sqlite
```

## Cara Menjalankan

### 1. Menjalankan migrasi

```bash
# Generate migration file (sudah dilakukan)
alembic -c development.ini revision --autogenerate -m "Create matakuliah table"

# Jalankan migration
alembic -c development.ini upgrade head
```

### 2. Menjalankan server

```bash
pserve development.ini --reload
```

Server akan berjalan di `http://localhost:6543`
## Model Data

## API Endpoints

Implementasi endpoint untuk operasi dasar:

| HTTP Method | URL Pattern            | Deskripsi                        |
|-------------|------------------------|----------------------------------|
| GET         | `/api/matakuliah`      | Mendapatkan semua matakuliah     |
| GET         | `/api/matakuliah/{id}` | Mendapatkan detail satu matakuliah|
| POST        | `/api/matakuliah`      | Menambahkan matakuliah baru      |
| PUT         | `/api/matakuliah/{id}` | Mengupdate data matakuliah       |
| DELETE      | `/api/matakuliah/{id}` | Menghapus data matakuliah        |
## Testing

### Tambahkan data awal minimal 4 matakuliah

### 1. GET 

melihat semua data matakuliah yang tersimpan di database.

**Endpoint:** `GET http://localhost:6543/api/models`

**Screenshot Testing:**

<img width="557" height="536" alt="Screenshot 2025-12-07 215240" src="https://github.com/user-attachments/assets/ce83be00-df73-4697-944d-52224c1f8b51" />

**Contoh Response:**
```json
{
    "success": true,
    "message": "Data ditemukan: 4",
    "data": [
        {
            "id": 1,
            "name": "Algoritma dan Pemrograman",
            "value": 3
        },
        {
            "id": 2,
            "name": "Basis Data",
            "value": 4
        },
        {
            "id": 3,
            "name": "Jaringan Komputer",
            "value": 3
        },
        {
            "id": 4,
            "name": "Keamanan Informasi",
            "value": 3
        }
    ]
}
```

---

### 2. POST

Menambahkan matakuliah baru ke database.

**Endpoint:** `http://localhost:6543/api/models`


**Request Body:**
```json
{
  "name": "Web Development",
  "value": 4
}
```

**Screenshot Testing:**

<img width="1381" height="456" alt="image" src="https://github.com/user-attachments/assets/de56af46-6a53-4715-bdf1-e51f1bd0caaa" />

---

### 3. PUT 

Mengupdate data matakuliah yang sudah ada.

**Endpoint:** `http://localhost:6543/api/models/1`

**Request Body:**
```json
{
  "name": "Algoritma Lanjut",
  "value": 5
}
```

**Screenshot Testing:**

<img width="1390" height="792" alt="image" src="https://github.com/user-attachments/assets/a52cdbfe-0b62-4d15-9605-9eb0fd7e14f1" />

---

### 4. DELETE 

Menghapus matakuliah dari database.

**Endpoint:** `http://localhost:6543/api/models/1`

**Screenshot Testing:**

<img width="1127" height="880" alt="Screenshot 2025-12-07 220003" src="https://github.com/user-attachments/assets/3dbfea00-9432-4a56-98fb-ee7043ac5c49" />

**Response (200 OK):**
```json
{
  "success":true,
  "message": "Data ID 1 berhasil dihapus"
}
```

---

### Cara Testing dengan Postman

1. Buka Postman
2. Pastikan server sudah running di `http://localhost:6543`
3. Buat request sesuai dengan endpoint di atas
4. Untuk POST dan PUT, jangan lupa set Header `Content-Type: application/json`
5. Screenshot setiap hasil testing untuk dokumentasi
6. Simpan screenshot di folder `screenshots/`

```

## Teknologi yang Digunakan

- **Framework:** Pyramid 2.0
- **Database:** SQLite (via SQLAlchemy)
- **Migration:** Alembic
- **Server:** Waitress
