# PostgreSQL Setup untuk Pertemuan6 - RINGKASAN LENGKAP

## 📦 File yang Sudah Dibuat/Dimodifikasi:

### ✅ File yang Dimodifikasi:

1. **setup.py**
   - Penambahan: `psycopg2-binary` ke dalam `requires` list
   - Tujuan: Driver untuk koneksi PostgreSQL

2. **development.ini**
   - Sebelum: `sqlalchemy.url = sqlite:///%(here)s/pertemuan6.sqlite`
   - Sesudah: `sqlalchemy.url = postgresql://username:password@localhost:5432/pertemuan6`

3. **production.ini**
   - Sebelum: `sqlalchemy.url = sqlite:///%(here)s/pertemuan6.sqlite`
   - Sesudah: `sqlalchemy.url = postgresql://username:password@localhost:5432/pertemuan6`

### 🆕 File yang Dibuat:

1. **DATABASE_SETUP.md** - Panduan lengkap setup PostgreSQL
   - Instalasi PostgreSQL
   - Membuat database dan user
   - Konfigurasi connection string
   - Testing koneksi
   - Troubleshooting

2. **POSTGRES_CONFIG.md** - Quick reference guide
   - Checklist setup
   - Quick start commands
   - Connection string format
   - Testing commands

3. **db_helper.py** - Python helper script
   - Test koneksi database
   - Display database info & tables
   - Usage: `python pertemuan6/db_helper.py test` atau `info`

4. **.env.example** - Environment variables template
   - Template untuk konfigurasi lokal
   - Copy ke `.env` untuk digunakan

5. **setup-postgres.ps1** - PowerShell automation script
   - Untuk Windows users
   - Auto-create database & user
   - Auto-update development.ini
   - Auto-install dependencies

6. **setup-database.sql** - SQL setup script
   - Untuk manual setup di PostgreSQL
   - Jalankan dengan: `psql -U postgres -f setup-database.sql`

---

## 🚀 CARA MEMULAI (3 OPSI):

### OPSI A: PowerShell Script (Recommended untuk Windows)

1. Buka PowerShell di direktori project
2. Jalankan: `.\setup-postgres.ps1`
3. Ikuti prompts untuk:
   - Input PostgreSQL credentials
   - Set database name
   - Set user credentials
4. Script akan otomatis:
   - Create database dan user
   - Update development.ini
   - Install dependencies

### OPSI B: SQL Script (Manual tapi cepat)

1. Buka PostgreSQL command prompt
2. Jalankan: `psql -U postgres -f setup-database.sql`
3. Edit development.ini sesuaikan connection string
4. Run: `pip install -e .`
5. Run: `python pertemuan6/scripts/initialize_db.py development.ini`

### OPSI C: Manual Step-by-Step

```bash
# 1. Install PostgreSQL dari: https://www.postgresql.org/download/

# 2. Buat database & user (di PostgreSQL terminal):
psql -U postgres
CREATE DATABASE pertemuan6;
CREATE USER pertemuan6_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE pertemuan6 TO pertemuan6_user;
\q

# 3. Update development.ini
# Edit file dan ubah sqlalchemy.url menjadi:
# sqlalchemy.url = postgresql://pertemuan6_user:your_password@localhost:5432/pertemuan6

# 4. Install dependencies
pip install -e .

# 5. Initialize database
python pertemuan6/scripts/initialize_db.py development.ini

# 6. Test koneksi
python pertemuan6/db_helper.py test

# 7. Run server
pserve development.ini
```

---

## 🔧 KONFIGURASI CONNECTION STRING:

**Format:**
```
postgresql://[user]:[password]@[host]:[port]/[database]
```

**Contoh:**
- Dengan user khusus: `postgresql://pertemuan6_user:mypassword@localhost:5432/pertemuan6`
- Dengan user postgres: `postgresql://postgres:postgres_password@localhost:5432/pertemuan6`
- Dengan environment variable: Gunakan `${DATABASE_URL}` di .env

---

## ✅ VERIFICATION CHECKLIST:

Pastikan langkah-langkah berikut berhasil:

- [ ] PostgreSQL terinstall (`psql --version`)
- [ ] Database created (`psql -U postgres -l | grep pertemuan6`)
- [ ] User created dengan privilege yang benar
- [ ] development.ini sudah di-update
- [ ] Dependencies installed (`pip list | grep psycopg2`)
- [ ] Connection test berhasil (`python pertemuan6/db_helper.py test`)
- [ ] Database tables created (`python pertemuan6/db_helper.py info`)
- [ ] Server running (`pserve development.ini`)

---

## 📋 TROUBLESHOOTING CEPAT:

| Masalah | Solusi |
|---------|--------|
| `psycopg2 not found` | `pip install psycopg2-binary` |
| `could not connect to server` | Check PostgreSQL service running |
| `password authentication failed` | Verify user & password di development.ini |
| `database does not exist` | Run database creation commands |
| `permission denied` | Grant privileges: `GRANT ALL PRIVILEGES ON DATABASE pertemuan6 TO user;` |

Untuk troubleshooting lebih detail, baca **DATABASE_SETUP.md**

---

## 📚 DOKUMENTASI:

- **DATABASE_SETUP.md** - Panduan lengkap (BACA INI!)
- **POSTGRES_CONFIG.md** - Quick reference
- **setup-postgres.ps1** - Script otomatis
- **db_helper.py** - Testing tool
- **.env.example** - Konfigurasi variables

---

## 🎯 NEXT STEPS:

1. Pilih salah satu opsi setup di atas
2. Jalankan sampai semua checklist terceklis
3. Test koneksi dengan `python pertemuan6/db_helper.py test`
4. Jalankan server dengan `pserve development.ini`
5. Akses aplikasi di `http://localhost:6543`

---

## 🆘 BANTUAN LEBIH LANJUT:

Jika ada error:
1. Baca **DATABASE_SETUP.md** untuk troubleshooting detail
2. Jalankan `python pertemuan6/db_helper.py info` untuk debug info
3. Check PostgreSQL logs di installation directory
4. Verify service running: Windows Services > postgresql-x64

---

**Setup PostgreSQL selesai! Database siap digunakan! 🎉**

Untuk pertanyaan lebih lanjut, baca dokumentasi file-file di atas.
