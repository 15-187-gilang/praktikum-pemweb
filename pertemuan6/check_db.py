import psycopg2

conn = psycopg2.connect('postgresql://pertemuan6_user:pertemuan6123@localhost:5432/pertemuan6')
cur = conn.cursor()

# List tables
cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema='public'""")
tables = cur.fetchall()

print("✓ Koneksi ke database BERHASIL!\n")
print(f"Total tables: {len(tables)}")

if tables:
    for table in tables:
        print(f"  - {table[0]}")
    
    # Check models table
    print("\nStructure table 'models':")
    cur.execute("""SELECT column_name, data_type FROM information_schema.columns WHERE table_name='models'""")
    columns = cur.fetchall()
    for col in columns:
        print(f"  - {col[0]}: {col[1]}")
else:
    print("  (belum ada tables)")
    print("\n⚠️ Jalankan: python -m pertemuan6.scripts.initialize_db development.ini")

conn.close()
