"""
Database configuration helper untuk PostgreSQL
"""
import os
import sys
from sqlalchemy import create_engine, inspect

def get_database_url():
    """
    Ambil database URL dari development.ini atau environment variable
    """
    # Coba dari environment variable dulu
    db_url = os.environ.get('DATABASE_URL')
    if db_url:
        return db_url
    
    # Default ke development.ini
    from pyramid.path import DottedNameResolver
    try:
        from pyramid.config import Configurator
        resolver = DottedNameResolver()
        settings = resolver.resolve('development:development')
        return settings.get('sqlalchemy.url', 'postgresql://postgres:password@localhost:5432/pertemuan6')
    except:
        return 'postgresql://postgres:password@localhost:5432/pertemuan6'

def test_connection(url=None):
    """
    Test koneksi ke database PostgreSQL
    """
    if url is None:
        url = get_database_url()
    
    try:
        engine = create_engine(url)
        connection = engine.connect()
        connection.close()
        print(f"✓ Koneksi berhasil ke: {url}")
        return True
    except Exception as e:
        print(f"✗ Gagal terhubung: {str(e)}")
        return False

def get_database_info(url=None):
    """
    Tampilkan informasi database
    """
    if url is None:
        url = get_database_url()
    
    try:
        engine = create_engine(url)
        inspector = inspect(engine)
        
        print(f"\nDatabase URL: {url}")
        print(f"Tables yang ada:")
        for table_name in inspector.get_table_names():
            print(f"  - {table_name}")
            columns = inspector.get_columns(table_name)
            for col in columns:
                col_type = str(col['type'])
                nullable = "NULL" if col['nullable'] else "NOT NULL"
                print(f"      * {col['name']}: {col_type} {nullable}")
        
        engine.dispose()
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            test_connection()
        elif sys.argv[1] == 'info':
            get_database_info()
        else:
            print("Usage:")
            print("  python db_helper.py test   - Test koneksi database")
            print("  python db_helper.py info   - Tampilkan info database")
    else:
        test_connection()
        print()
        get_database_info()
