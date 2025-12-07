# PostgreSQL Configuration untuk Pertemuan6

> **⚠️ BACA DULU: [INDEX.md](INDEX.md)** untuk dokumentasi lengkap

## 📋 RINGKASAN SINGKAT

Proyek ini sudah dikonfigurasi untuk menggunakan **PostgreSQL** sebagai database. Berikut file yang telah dimodifikasi:

### ✏️ File yang Dimodifikasi:
1. **setup.py** - Ditambah `psycopg2-binary` driver
2. **development.ini** - Connection string diubah ke PostgreSQL  
3. **production.ini** - Connection string diubah ke PostgreSQL

### 🆕 File yang Dibuat:
- **Dokumentasi**: DATABASE_SETUP.md, QUICKSTART.md, POSTGRES_CONFIG.md, dll
- **Tools**: setup-postgres.ps1, verify_postgres_setup.py, db_helper.py
- **Konfigurasi**: .env.example, setup-database.sql

---

## 🚀 SETUP CEPAT (Pilih 1)

### ✅ OPSI A: Windows PowerShell (Recommended)
```powershell
.\setup-postgres.ps1
```
Script ini akan otomatis:
- ✓ Detect PostgreSQL installation
- ✓ Create database & user
- ✓ Update development.ini
- ✓ Install Python dependencies

### ✅ OPSI B: Manual dengan SQL Script
```bash
psql -U postgres -f setup-database.sql
# Edit development.ini connection string
pip install -e .
python pertemuan6/scripts/initialize_db.py development.ini
```

### ✅ OPSI C: Step-by-Step Manual
Lihat [QUICKSTART.md](QUICKSTART.md) untuk detail lengkap

---

## 🔧 CONNECTION STRING

Format: `postgresql://[user]:[password]@[host]:[port]/[dbname]`

**Contoh:**
```ini
sqlalchemy.url = postgresql://pertemuan6_user:mypassword@localhost:5432/pertemuan6
```

---

## ✅ VERIFIKASI SETUP

```bash
# Verifikasi lengkap
python verify_postgres_setup.py

# Test koneksi database
python db_helper.py test

# Lihat info database
python db_helper.py info
```

---

## 📚 DOKUMENTASI

| Dokumen | Tujuan |
|---------|--------|
| [INDEX.md](INDEX.md) | 📌 **BACA INI DULU** - Navigation guide |
| [SETUP_SUMMARY.txt](SETUP_SUMMARY.txt) | Quick visual summary |
| [QUICKSTART.md](QUICKSTART.md) | 5-menit setup guide |
| [DATABASE_SETUP.md](DATABASE_SETUP.md) | Panduan lengkap & troubleshooting |
| [POSTGRES_CONFIG.md](POSTGRES_CONFIG.md) | Quick reference |
| [FILE_MANIFEST.md](FILE_MANIFEST.md) | Daftar lengkap semua file |

---

## 🛠️ TOOLS

| Script | Fungsi | Command |
|--------|--------|---------|
| setup-postgres.ps1 | Auto-setup (Windows) | `.\setup-postgres.ps1` |
| setup-database.sql | Manual setup (SQL) | `psql -U postgres -f setup-database.sql` |
| verify_postgres_setup.py | Verify installation | `python verify_postgres_setup.py` |
| db_helper.py | Test & debug | `python db_helper.py test` |

---

## 📖 DOKUMENTASI LENGKAP

**Untuk Setup Detail:**
→ Baca [DATABASE_SETUP.md](DATABASE_SETUP.md)

**Untuk Quick Reference:**
→ Baca [POSTGRES_CONFIG.md](POSTGRES_CONFIG.md)

**Untuk File Overview:**
→ Baca [FILE_MANIFEST.md](FILE_MANIFEST.md)

**Untuk Navigation:**
→ Baca [INDEX.md](INDEX.md) ← **START HERE!**

---

## ⚡ COMMON COMMANDS

```bash
# Jalankan development server
pserve development.ini

# Test dengan pytest
pytest pertemuan6/tests.py

# Connect ke database dengan psql
psql -U pertemuan6_user -d pertemuan6

# Initialize database
python pertemuan6/scripts/initialize_db.py development.ini

# Backup database
pg_dump -U pertemuan6_user -d pertemuan6 > backup.sql
```

---

## ❓ FAQ

**Q: Apa yang sudah di-setup?**
A: PostgreSQL driver, connection string, dan documentation lengkap.

**Q: Saya harus install apa?**
A: PostgreSQL server di system Anda. Setup script akan create database & user.

**Q: Bagaimana cara memulai?**
A: 
1. Baca [INDEX.md](INDEX.md)
2. Jalankan setup dari [QUICKSTART.md](QUICKSTART.md)
3. Verifikasi dengan `python verify_postgres_setup.py`

**Q: Ada error, gimana?**
A: Baca troubleshooting di [DATABASE_SETUP.md](DATABASE_SETUP.md)

---

## 🎯 NEXT STEPS

1. ✅ **Baca:** [INDEX.md](INDEX.md) atau [SETUP_SUMMARY.txt](SETUP_SUMMARY.txt)
2. ✅ **Setup:** Pilih opsi dari [QUICKSTART.md](QUICKSTART.md)
3. ✅ **Verifikasi:** `python verify_postgres_setup.py`
4. ✅ **Test:** `python db_helper.py test`
5. ✅ **Run:** `pserve development.ini`

---

## 📞 BANTUAN

- **Setup Issues** → [DATABASE_SETUP.md](DATABASE_SETUP.md)
- **Quick Commands** → [POSTGRES_CONFIG.md](POSTGRES_CONFIG.md)
- **File Overview** → [FILE_MANIFEST.md](FILE_MANIFEST.md)
- **Navigation** → [INDEX.md](INDEX.md)

---

**🚀 PostgreSQL setup selesai! Happy coding!**

**👉 Baca [INDEX.md](INDEX.md) untuk dokumentasi lengkap**
