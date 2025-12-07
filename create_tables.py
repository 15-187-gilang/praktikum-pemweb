#!/usr/bin/env python
"""
Script untuk membuat tabel dan insert sample data ke database PostgreSQL
"""
import psycopg2
from psycopg2 import sql

# Database connection settings
db_config = {
    'host': 'localhost',
    'database': 'pertemuan6',
    'user': 'pertemuan6_user',
    'password': 'pertemuan6123',
    'port': 5432
}

try:
    # Koneksi ke database
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()
    
    print("✓ Koneksi ke database berhasil")
    
    # Drop tabel jika sudah ada (untuk clean slate)
    cursor.execute("DROP TABLE IF EXISTS models CASCADE;")
    print("✓ Tabel lama dihapus (jika ada)")
    
    # Buat tabel models
    create_table_query = """
    CREATE TABLE models (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        value INTEGER NOT NULL
    );
    """
    cursor.execute(create_table_query)
    print("✓ Tabel 'models' berhasil dibuat")
    
    # Insert 4 sample data
    sample_data = [
        ("Algoritma dan Pemrograman", 3),
        ("Basis Data", 4),
        ("Jaringan Komputer", 3),
        ("Keamanan Informasi", 3)
    ]
    
    insert_query = "INSERT INTO models (name, value) VALUES (%s, %s);"
    
    for name, value in sample_data:
        cursor.execute(insert_query, (name, value))
        print(f"✓ Insert: '{name}' dengan value {value}")
    
    # Commit semua perubahan
    conn.commit()
    
    # Verifikasi data yang sudah diinsert
    cursor.execute("SELECT * FROM models;")
    rows = cursor.fetchall()
    
    print("\n" + "="*60)
    print("DATA YANG SUDAH DIINSERT:")
    print("="*60)
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Value: {row[2]}")
    
    print("="*60)
    print(f"✓ Total {len(rows)} data berhasil diinsert")
    print("="*60)
    
    cursor.close()
    conn.close()
    print("✓ Koneksi ditutup")
    
except Exception as e:
    print(f"✗ Error: {e}")
    if conn:
        conn.rollback()
