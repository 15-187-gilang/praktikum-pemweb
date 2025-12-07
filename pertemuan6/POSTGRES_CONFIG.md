## Konfigurasi PostgreSQL - Pertemuan6

### 📋 File-file yang Sudah Dikonfigurasi:

1. **setup.py** ✓
   - Ditambahkan: `psycopg2-binary` (driver PostgreSQL)

2. **development.ini** ✓
   - Diubah: `sqlalchemy.url = postgresql://username:password@localhost:5432/pertemuan6`

3. **DATABASE_SETUP.md** ✓ (BARU)
   - Panduan lengkap setup PostgreSQL
   - Troubleshooting tips
   - Environment variables configuration

4. **db_helper.py** ✓ (BARU)
   - Script helper untuk test koneksi database
   - Tampilkan info database dan tables

5. **.env.example** ✓ (BARU)
   - Template environment variables
   - Copy ke `.env` untuk konfigurasi lokal

6. **setup-postgres.ps1** ✓ (BARU)
   - Script PowerShell otomatis untuk Windows
   - Membuat database dan user PostgreSQL

---

### 🚀 QUICK START - Cara Menggunakan:

#### Opsi 1: Menggunakan Script PowerShell (RECOMMENDED untuk Windows)
```powershell
# Jalankan di direktori project
.\setup-postgres.ps1
```

Script ini akan:
- ✓ Detect PostgreSQL installation
- ✓ Create database
- ✓ Create user
- ✓ Update development.ini
- ✓ Install Python dependencies

#### Opsi 2: Setup Manual

**Step 1: Instal PostgreSQL**
- Download dari: https://www.postgresql.org/download/

**Step 2: Buat Database di PostgreSQL**
```sql
psql -U postgres

CREATE DATABASE pertemuan6;
CREATE USER pertemuan6_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE pertemuan6 TO pertemuan6_user;
```

**Step 3: Update development.ini**
Ubah baris `sqlalchemy.url` menjadi:
```ini
sqlalchemy.url = postgresql://pertemuan6_user:your_password@localhost:5432/pertemuan6
```

**Step 4: Install Dependencies**
```bash
pip install -e .
```

**Step 5: Initialize Database**
```bash
python pertemuan6/scripts/initialize_db.py development.ini
```

**Step 6: Test Connection**
```bash
python -c "from pertemuan6.db_helper import test_connection; test_connection()"
```

---

### 📝 Connection String Format:

```
postgresql://[user[:password]@][host][:port][/dbname]
```

Contoh:
- `postgresql://postgres:password@localhost:5432/pertemuan6`
- `postgresql://pertemuan6_user:your_pass@localhost:5432/pertemuan6`

---

### 🔍 Testing Koneksi:

**Dengan Python:**
```bash
python pertemuan6/db_helper.py test
python pertemuan6/db_helper.py info
```

**Dengan psql:**
```bash
psql -U pertemuan6_user -d pertemuan6 -h localhost
```

---

### 📚 File Documentation:

Baca `DATABASE_SETUP.md` untuk panduan lengkap termasuk:
- Troubleshooting
- Advanced configuration
- Multiple environment setup
- Security best practices

---

### ⚙️ Konfigurasi Production:

Update `production.ini` dengan connection string yang aman:
```ini
sqlalchemy.url = postgresql://pertemuan6_user:secure_password@prod-server:5432/pertemuan6_prod
```

---

### 🎯 Model Data (Sudah Dikonfigurasi):

File: `pertemuan6/models/mymodel.py`

```python
class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)
```

Tables akan otomatis dibuat saat migration dijalankan.

---

### ✅ Checklist Setup:

- [ ] PostgreSQL terinstall
- [ ] Database dan user dibuat
- [ ] development.ini dikonfigurasi
- [ ] `pip install -e .` berhasil
- [ ] initialize_db.py berhasil dijalankan
- [ ] Test koneksi berhasil
- [ ] Server berjalan dengan `pserve development.ini`

---

### 🆘 Bantuan:

1. Baca `DATABASE_SETUP.md` untuk troubleshooting
2. Jalankan `python pertemuan6/db_helper.py info`
3. Check PostgreSQL service status di Windows Services
4. Verify user privileges di pgAdmin atau psql

---

**Setup selesai! Happy coding! 🎉**
