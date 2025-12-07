-- PostgreSQL Setup Script untuk Pertemuan6
-- Jalankan dengan: psql -U postgres -f setup-pertemuan6.sql

-- 1. DROP existing if exists (optional)
DROP DATABASE IF EXISTS pertemuan6;
DROP USER IF EXISTS pertemuan6_user;

-- 2. CREATE DATABASE
CREATE DATABASE pertemuan6;

-- 3. CREATE USER
CREATE USER pertemuan6_user WITH PASSWORD 'pertemuan6123';

-- 3. GRANT PRIVILEGES
GRANT ALL PRIVILEGES ON DATABASE pertemuan6 TO pertemuan6_user;

-- 4. Connect to database
\c pertemuan6

-- 5. Grant schema privileges
GRANT ALL PRIVILEGES ON SCHEMA public TO pertemuan6_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO pertemuan6_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO pertemuan6_user;

-- 6. Verify
SELECT 'Database pertemuan6 dan user pertemuan6_user berhasil dibuat!' as status;
