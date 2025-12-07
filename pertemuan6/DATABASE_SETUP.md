# Setup PostgreSQL untuk Pertemuan6

## Prasyarat
Pastikan PostgreSQL sudah terinstall di sistem Anda. Jika belum, download dari: https://www.postgresql.org/download/

## Langkah-Langkah Setup

### 1. Buat Database PostgreSQL
Buka PostgreSQL terminal atau command prompt dan jalankan:

```sql
-- Login ke PostgreSQL dengan user postgres
psql -U postgres

-- Buat database baru
CREATE DATABASE pertemuan6;

-- Buat user baru (opsional, untuk keamanan lebih baik)
CREATE USER pertemuan6_user WITH PASSWORD 'your_password';

-- Berikan privilege ke user
GRANT ALL PRIVILEGES ON DATABASE pertemuan6 TO pertemuan6_user;
```

### 2. Update development.ini
Edit file `development.ini` dan sesuaikan connection string:

```ini
# Format: postgresql://username:password@localhost:5432/database_name

# Jika menggunakan user postgres (default)
sqlalchemy.url = postgresql://postgres:your_postgres_password@localhost:5432/pertemuan6

# Jika menggunakan user khusus yang dibuat
sqlalchemy.url = postgresql://pertemuan6_user:your_password@localhost:5432/pertemuan6
```

### 3. Update production.ini (jika ada)
Lakukan hal yang sama untuk `production.ini`

### 4. Install Dependencies
Jalankan di terminal (di direktori project):

```bash
# Install requirements termasuk psycopg2 driver PostgreSQL
pip install -e .

# Atau jika sudah ada environment
python -m pip install -e .
```

### 5. Setup Database dengan Alembic
Jalankan migrasi database:

```bash
# Upgrade ke latest version
alembic upgrade head

# Atau inisialisasi database
python pertemuan6/scripts/initialize_db.py development.ini
```

### 6. Test Connection
Untuk memastikan koneksi berhasil, jalankan:

```bash
pshell development.ini
```

Di dalam pshell, coba:
```python
from pertemuan6.models import MyModel
# Jika berhasil, tidak ada error
```

## Troubleshooting

### Error: "psycopg2" is not installed
Solusi: 
```bash
pip install psycopg2-binary
```

### Error: could not connect to server
- Periksa apakah PostgreSQL service sudah running
- Periksa kredensial username/password
- Periksa bahwa database sudah dibuat
- Periksa port (default 5432)

### Error: permission denied
Periksa grant privilege:
```sql
GRANT ALL PRIVILEGES ON DATABASE pertemuan6 TO pertemuan6_user;
```

## Database Connection String Format

```
postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
```

Contoh:
- `postgresql://postgres:password@localhost:5432/pertemuan6`
- `postgresql://user:pass@192.168.1.100:5432/mydb`
- `postgresql://localhost/pertemuan6` (tanpa user/pass, menggunakan peer authentication)

## Environment Variables (Opsional)
Anda juga bisa menggunakan environment variable:

```bash
# Windows PowerShell
$env:DATABASE_URL = "postgresql://user:password@localhost:5432/pertemuan6"

# Linux/Mac
export DATABASE_URL="postgresql://user:password@localhost:5432/pertemuan6"
```

Kemudian di development.ini:
```ini
sqlalchemy.url = %(DATABASE_URL)s
```

## Verifikasi Setup

1. Buka PostgreSQL psql client:
```bash
psql -U pertemuan6_user -d pertemuan6 -h localhost
```

2. List tables:
```sql
\dt
```

3. Keluar:
```sql
\q
```

Selamat! PostgreSQL sudah siap digunakan untuk project Pertemuan6.
