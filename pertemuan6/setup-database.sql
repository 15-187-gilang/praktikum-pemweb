-- PostgreSQL Setup Script untuk Pertemuan6
-- Jalankan ini di PostgreSQL dengan user postgres:
--   psql -U postgres -f setup-database.sql

-- ============================================
-- 1. CREATE DATABASE
-- ============================================
CREATE DATABASE IF NOT EXISTS pertemuan6;
\c pertemuan6

-- ============================================
-- 2. CREATE USER (uncomment jika ingin user baru)
-- ============================================
-- CREATE USER pertemuan6_user WITH PASSWORD 'your_secure_password';
-- GRANT ALL PRIVILEGES ON DATABASE pertemuan6 TO pertemuan6_user;

-- ============================================
-- 3. CREATE SCHEMA
-- ============================================
CREATE SCHEMA IF NOT EXISTS public;

-- ============================================
-- 4. GRANT PRIVILEGES
-- ============================================
-- Uncomment dan sesuaikan dengan username Anda:
-- GRANT ALL PRIVILEGES ON SCHEMA public TO pertemuan6_user;
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO pertemuan6_user;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO pertemuan6_user;

-- ============================================
-- 5. CREATE TABLES (akan dibuat oleh alembic)
-- ============================================
-- Tables akan otomatis dibuat saat Anda menjalankan:
-- python pertemuan6/scripts/initialize_db.py development.ini

-- ============================================
-- 6. VERIFY
-- ============================================
SELECT 'Database pertemuan6 berhasil dibuat!' as status;
\dt

-- ============================================
-- KONFIGURASI SELESAI
-- ============================================
-- Langkah selanjutnya:
-- 1. Edit development.ini dan atur connection string
-- 2. Jalankan: python pertemuan6/scripts/initialize_db.py development.ini
-- 3. Jalankan: pserve development.ini
