# PostgreSQL Quick Start Guide - Pertemuan6

## 🎯 5-MENIT SETUP (Pilih 1 Opsi)

### ✅ OPSI TERCEPAT (Windows)

```powershell
# Buka PowerShell di project directory
.\setup-postgres.ps1

# Ikuti prompts (username, password, database name)
# Selesai! Script akan:
# - Create database & user
# - Update development.ini
# - Install dependencies
```

### ✅ OPSI LINUX/MAC

```bash
# 1. Install PostgreSQL (jika belum)
brew install postgresql  # macOS
# atau
sudo apt-get install postgresql postgresql-contrib  # Linux

# 2. Start PostgreSQL service
brew services start postgresql  # macOS
# atau
sudo systemctl start postgresql  # Linux

# 3. Create database
createdb pertemuan6
createuser -P pertemuan6_user  # Enter password when prompted

# 4. Grant privileges
psql pertemuan6 << EOF
GRANT ALL PRIVILEGES ON DATABASE pertemuan6 TO pertemuan6_user;
\q
EOF

# 5. Update development.ini
# Edit dan ubah sqlalchemy.url menjadi:
# sqlalchemy.url = postgresql://pertemuan6_user:your_password@localhost:5432/pertemuan6

# 6. Install & Initialize
pip install -e .
python pertemuan6/scripts/initialize_db.py development.ini

# 7. Run server
pserve development.ini
```

---

## 🔍 VERIFICATION (Setelah Setup)

```bash
# Test koneksi database
python pertemuan6/db_helper.py test

# Lihat database info & tables
python pertemuan6/db_helper.py info

# Jalankan verification script
python verify_postgres_setup.py
```

---

## ⚡ COMMON COMMANDS

```bash
# Start server
pserve development.ini

# Stop server: Press Ctrl+C

# Access shell prompt
pshell development.ini

# Run migrations
alembic upgrade head

# Create new migration
alembic revision --autogenerate -m "Add new column"

# Initialize database
python pertemuan6/scripts/initialize_db.py development.ini

# Test with pytest
pytest pertemuan6/tests.py
```

---

## 🗄️ DATABASE MANAGEMENT

### Via PostgreSQL client
```bash
# Connect to database
psql -U pertemuan6_user -d pertemuan6

# List tables
\dt

# View table structure
\d models

# Exit
\q
```

### Via pgAdmin (GUI)
1. Download: https://www.pgadmin.org/download/
2. Launch pgAdmin
3. Create server connection:
   - Name: pertemuan6
   - Host: localhost
   - Port: 5432
   - User: pertemuan6_user
   - Password: your_password
4. Browse databases & tables visually

---

## 🛠️ CONNECTION STRING

**Jika menggunakan opsi setup:**
```
postgresql://pertemuan6_user:your_password@localhost:5432/pertemuan6
```

**Untuk keamanan:**
```bash
# Gunakan environment variable
export DATABASE_URL="postgresql://user:password@host:port/dbname"

# Di development.ini:
sqlalchemy.url = ${DATABASE_URL}
```

---

## 🐛 TROUBLESHOOTING CEPAT

| Error | Solusi |
|-------|--------|
| `ModuleNotFoundError: No module named 'psycopg2'` | `pip install psycopg2-binary` |
| `could not connect to server` | PostgreSQL service not running |
| `password authentication failed` | Wrong password di development.ini |
| `database "pertemuan6" does not exist` | Run database creation commands |
| `permission denied for schema public` | Grant privileges dengan GRANT command |

---

## 📚 FULL DOCUMENTATION

Untuk setup detail & troubleshooting lengkap:
- **DATABASE_SETUP.md** - Panduan komprehensif
- **POSTGRES_CONFIG.md** - Quick reference
- **POSTGRES_SETUP_README.md** - Ringkasan semua opsi

---

## 🚀 NEXT STEPS

1. ✅ Setup PostgreSQL (pilih opsi di atas)
2. ✅ Verify dengan `python verify_postgres_setup.py`
3. ✅ Jalankan server: `pserve development.ini`
4. ✅ Test aplikasi di `http://localhost:6543`
5. ✅ Backup development credentials untuk production

---

## 💾 BACKUP DATABASE

```bash
# Export database ke file
pg_dump -U pertemuan6_user -d pertemuan6 > backup.sql

# Import database dari file
psql -U pertemuan6_user -d pertemuan6 < backup.sql
```

---

## 🎓 LEARNING RESOURCES

- SQLAlchemy: https://docs.sqlalchemy.org/
- Alembic: https://alembic.zzzcomputing.com/
- PostgreSQL: https://www.postgresql.org/docs/
- Pyramid: https://docs.pylonsproject.org/

---

**Happy coding dengan PostgreSQL! 🎉**

Jika ada pertanyaan, baca dokumentasi file atau check troubleshooting.
