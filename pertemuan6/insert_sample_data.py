#!/usr/bin/env python
"""
Script untuk insert sample data ke database
"""
import psycopg2

conn = psycopg2.connect('postgresql://pertemuan6_user:pertemuan6123@localhost:5432/pertemuan6')
cur = conn.cursor()

# Check if models table exists
cur.execute("""
    SELECT EXISTS (
        SELECT 1 FROM information_schema.tables 
        WHERE table_name='models'
    )
""")

table_exists = cur.fetchone()[0]

if not table_exists:
    print("❌ Table 'models' tidak ada!")
    print("Jalankan: python -m pertemuan6.scripts.initialize_db development.ini")
    conn.close()
    exit(1)

# Sample data
sample_data = [
    ('Algoritma dan Pemrograman', 3),
    ('Struktur Data', 4),
    ('Database Management System', 3),
    ('Web Programming', 4),
    ('Mobile Development', 3),
]

# Insert data
try:
    for name, value in sample_data:
        cur.execute(
            "INSERT INTO models (name, value) VALUES (%s, %s)",
            (name, value)
        )
    
    conn.commit()
    print(f"✅ {len(sample_data)} data berhasil diinsert ke database!")
    
    # Display inserted data
    cur.execute("SELECT id, name, value FROM models ORDER BY id")
    rows = cur.fetchall()
    print(f"\nData di database:")
    for row in rows:
        print(f"  ID {row[0]}: {row[1]} (value: {row[2]})")
    
except Exception as e:
    conn.rollback()
    print(f"❌ Error: {e}")

finally:
    cur.close()
    conn.close()
