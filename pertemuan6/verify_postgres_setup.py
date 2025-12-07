#!/usr/bin/env python3
"""
PostgreSQL Setup Verification Script
Jalankan: python verify_postgres_setup.py
"""

import sys
import os
from pathlib import Path
from configparser import ConfigParser

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    print(f"\n{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{text:^60}{Colors.ENDC}")
    print(f"{Colors.BOLD}{Colors.HEADER}{'='*60}{Colors.ENDC}\n")

def print_check(text, status):
    symbol = f"{Colors.OKGREEN}✓{Colors.ENDC}" if status else f"{Colors.FAIL}✗{Colors.ENDC}"
    print(f"  {symbol} {text}")
    return status

def check_postgresql_installed():
    print_header("1. CHECK POSTGRESQL INSTALLATION")
    
    try:
        import psycopg2
        print_check("psycopg2 module terinstall", True)
        print(f"    Version: {psycopg2.__version__}")
        return True
    except ImportError:
        print_check("psycopg2 module terinstall", False)
        print(f"    {Colors.WARNING}Fix: pip install psycopg2-binary{Colors.ENDC}")
        return False

def check_development_ini():
    print_header("2. CHECK development.ini CONFIGURATION")
    
    dev_ini = Path("development.ini")
    if not dev_ini.exists():
        print_check(f"development.ini exists", False)
        return False
    
    print_check(f"development.ini exists", True)
    
    config = ConfigParser()
    config.read(dev_ini)
    
    try:
        db_url = config.get('app:main', 'sqlalchemy.url')
        print(f"    Connection: {db_url}")
        
        if 'postgresql' in db_url:
            print_check("Using PostgreSQL", True)
            return True
        elif 'sqlite' in db_url:
            print_check("Using SQLite (should be PostgreSQL)", False)
            print(f"    {Colors.WARNING}Update to PostgreSQL{Colors.ENDC}")
            return False
        else:
            print_check("Database type recognized", False)
            return False
    except:
        print_check("sqlalchemy.url configured", False)
        return False

def check_database_connection():
    print_header("3. CHECK DATABASE CONNECTION")
    
    try:
        import psycopg2
        from configparser import ConfigParser
        
        config = ConfigParser()
        config.read("development.ini")
        db_url = config.get('app:main', 'sqlalchemy.url')
        
        # Parse connection string
        # Format: postgresql://user:password@host:port/dbname
        if '://' in db_url:
            db_url = db_url.split('://')[1]
        
        if '@' in db_url:
            creds, host_db = db_url.split('@')
            user, password = creds.split(':') if ':' in creds else (creds, '')
        else:
            user = 'postgres'
            password = ''
            host_db = db_url
        
        if ':' in host_db:
            host, db_port_name = host_db.split(':')
            if '/' in db_port_name:
                port, dbname = db_port_name.split('/')
                port = int(port)
            else:
                port = 5432
                dbname = db_port_name
        else:
            host = 'localhost'
            port = 5432
            if '/' in host_db:
                host, dbname = host_db.split('/')
            else:
                dbname = host_db
        
        print(f"    Host: {host}")
        print(f"    Port: {port}")
        print(f"    Database: {dbname}")
        print(f"    User: {user}")
        
        # Try to connect
        try:
            conn = psycopg2.connect(
                host=host,
                port=port,
                database=dbname,
                user=user,
                password=password if password else None
            )
            print_check("Database connection successful", True)
            conn.close()
            return True
        except Exception as e:
            print_check("Database connection successful", False)
            print(f"    {Colors.WARNING}Error: {str(e)}{Colors.ENDC}")
            return False
            
    except Exception as e:
        print_check("Check connection", False)
        print(f"    {Colors.WARNING}Error: {str(e)}{Colors.ENDC}")
        return False

def check_sqlalchemy():
    print_header("4. CHECK SQLALCHEMY & ALEMBIC")
    
    status = True
    
    try:
        import sqlalchemy
        print_check("SQLAlchemy installed", True)
        print(f"    Version: {sqlalchemy.__version__}")
    except ImportError:
        print_check("SQLAlchemy installed", False)
        status = False
    
    try:
        import alembic
        print_check("Alembic installed", True)
        print(f"    Version: {alembic.__version__}")
    except ImportError:
        print_check("Alembic installed", False)
        status = False
    
    return status

def check_models():
    print_header("5. CHECK MODELS")
    
    mymodel_path = Path("pertemuan6/models/mymodel.py")
    if mymodel_path.exists():
        print_check("mymodel.py exists", True)
        # Try to import
        try:
            sys.path.insert(0, str(Path.cwd()))
            from pertemuan6.models.mymodel import MyModel
            print_check("MyModel class importable", True)
            print(f"    Table: {MyModel.__tablename__}")
            return True
        except Exception as e:
            print_check("MyModel class importable", False)
            print(f"    {Colors.WARNING}Error: {str(e)}{Colors.ENDC}")
            return False
    else:
        print_check("mymodel.py exists", False)
        return False

def check_documentation():
    print_header("6. CHECK DOCUMENTATION")
    
    docs = [
        "DATABASE_SETUP.md",
        "POSTGRES_CONFIG.md",
        "POSTGRES_SETUP_README.md",
        "SETUP_SUMMARY.txt"
    ]
    
    status = True
    for doc in docs:
        exists = Path(doc).exists()
        print_check(f"{doc}", exists)
        if not exists:
            status = False
    
    return status

def print_recommendations():
    print_header("RECOMMENDATIONS")
    
    print(f"{Colors.OKCYAN}Untuk setup PostgreSQL:{Colors.ENDC}")
    print(f"  1. Baca: DATABASE_SETUP.md")
    print(f"  2. Jalankan: .\setup-postgres.ps1")
    print(f"  3. Verify: python verify_postgres_setup.py (script ini)")
    print(f"  4. Run: pserve development.ini")
    print(f"\n{Colors.OKCYAN}Untuk testing koneksi:{Colors.ENDC}")
    print(f"  python pertemuan6/db_helper.py test")
    print(f"  python pertemuan6/db_helper.py info")

def main():
    print(f"\n{Colors.BOLD}{Colors.OKCYAN}")
    print("╔══════════════════════════════════════════════════════════╗")
    print("║     PostgreSQL Setup Verification - Pertemuan6           ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print(Colors.ENDC)
    
    results = []
    
    results.append(("PostgreSQL Installation", check_postgresql_installed()))
    results.append(("development.ini Configuration", check_development_ini()))
    results.append(("SQLAlchemy & Alembic", check_sqlalchemy()))
    results.append(("Models", check_models()))
    results.append(("Documentation", check_documentation()))
    
    try:
        results.append(("Database Connection", check_database_connection()))
    except:
        results.append(("Database Connection", False))
    
    # Summary
    print_header("SUMMARY")
    
    passed = sum(1 for _, status in results if status)
    total = len(results)
    
    for name, status in results:
        symbol = f"{Colors.OKGREEN}PASS{Colors.ENDC}" if status else f"{Colors.FAIL}FAIL{Colors.ENDC}"
        print(f"  {symbol} - {name}")
    
    print(f"\n  Total: {Colors.BOLD}{passed}/{total}{Colors.ENDC}")
    
    if passed == total:
        print(f"\n  {Colors.OKGREEN}{Colors.BOLD}✓ All checks passed!{Colors.ENDC}")
        print(f"  {Colors.OKGREEN}PostgreSQL setup OK!{Colors.ENDC}\n")
    else:
        print(f"\n  {Colors.WARNING}{Colors.BOLD}⚠ Some checks failed{Colors.ENDC}")
        print(f"  {Colors.WARNING}Baca dokumentasi untuk troubleshooting{Colors.ENDC}\n")
    
    print_recommendations()
    
    print(f"\n{Colors.BOLD}{Colors.OKCYAN}═══════════════════════════════════════════════════════════{Colors.ENDC}\n")

if __name__ == "__main__":
    main()
