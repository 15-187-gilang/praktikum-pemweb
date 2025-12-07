# Setup PostgreSQL untuk Pertemuan6
# Jalankan script ini dengan: .\setup-postgres.ps1

Write-Host "=== PostgreSQL Setup untuk Pertemuan6 ===" -ForegroundColor Cyan

# Check if PostgreSQL is installed
$pgPath = "C:\Program Files\PostgreSQL\*\bin\psql.exe"
$psqlExe = Get-Item $pgPath -ErrorAction SilentlyContinue | Select-Object -First 1

if (-not $psqlExe) {
    Write-Host "ERROR: PostgreSQL tidak ditemukan!" -ForegroundColor Red
    Write-Host "Silakan install PostgreSQL dari: https://www.postgresql.org/download/windows/" -ForegroundColor Yellow
    exit 1
}

$psqlPath = $psqlExe.FullName
Write-Host "✓ PostgreSQL ditemukan: $psqlPath" -ForegroundColor Green

# Get credentials
Write-Host "`nMasukkan kredensial PostgreSQL:" -ForegroundColor Cyan
$postgresUser = Read-Host "PostgreSQL User (default: postgres)"
if ([string]::IsNullOrEmpty($postgresUser)) { $postgresUser = "postgres" }

$postgresPassword = Read-Host "PostgreSQL Password" -AsSecureString
$postgresPassword = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($postgresPassword))

# Get new database user details
Write-Host "`nKonfigurasi User Baru (opsional):" -ForegroundColor Cyan
$newUser = Read-Host "Username baru (default: pertemuan6_user)"
if ([string]::IsNullOrEmpty($newUser)) { $newUser = "pertemuan6_user" }

$newPassword = Read-Host "Password user baru" -AsSecureString
$newPassword = [Runtime.InteropServices.Marshal]::PtrToStringAuto([Runtime.InteropServices.Marshal]::SecureStringToBSTR($newPassword))

$dbName = Read-Host "Database name (default: pertemuan6)"
if ([string]::IsNullOrEmpty($dbName)) { $dbName = "pertemuan6" }

Write-Host "`n=== Membuat Database dan User ===" -ForegroundColor Cyan

# Create SQL script
$sqlScript = @"
-- Buat database
CREATE DATABASE $dbName;

-- Buat user baru
CREATE USER $newUser WITH PASSWORD '$newPassword';

-- Berikan privileges
GRANT ALL PRIVILEGES ON DATABASE $dbName TO $newUser;

-- Alter default privileges
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO $newUser;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO $newUser;

-- Koneksi ke database baru
\c $dbName

-- Berikan privilege pada schema
GRANT ALL PRIVILEGES ON SCHEMA public TO $newUser;

-- Display hasil
SELECT version();
SELECT datname FROM pg_database WHERE datname = '$dbName';
"@

# Save SQL script to temp file
$tempSqlFile = "$env:TEMP\pertemuan6_setup.sql"
$sqlScript | Out-File -FilePath $tempSqlFile -Encoding UTF8

# Execute SQL script
try {
    $env:PGPASSWORD = $postgresPassword
    & $psqlPath -U $postgresUser -h localhost -f $tempSqlFile -v ON_ERROR_STOP=1
    Write-Host "✓ Database dan user berhasil dibuat!" -ForegroundColor Green
} catch {
    Write-Host "✗ Error: $_" -ForegroundColor Red
} finally {
    $env:PGPASSWORD = ""
    Remove-Item $tempSqlFile -Force -ErrorAction SilentlyContinue
}

# Update development.ini
Write-Host "`n=== Update development.ini ===" -ForegroundColor Cyan

$devIniPath = ".\development.ini"
if (Test-Path $devIniPath) {
    $content = Get-Content $devIniPath -Raw
    $newConnectionString = "postgresql://$newUser`:$newPassword@localhost:5432/$dbName"
    
    # Update atau tambah sqlalchemy.url
    if ($content -match "sqlalchemy\.url\s*=") {
        $content = $content -replace "sqlalchemy\.url\s*=.*", "sqlalchemy.url = $newConnectionString"
    } else {
        $content = $content -replace "(use = egg:pertemuan6)", "`$1`n`nsqlalchemy.url = $newConnectionString"
    }
    
    $content | Set-Content $devIniPath
    Write-Host "✓ development.ini berhasil diupdate" -ForegroundColor Green
} else {
    Write-Host "✗ development.ini tidak ditemukan" -ForegroundColor Red
}

# Install Python dependencies
Write-Host "`n=== Install Dependencies ===" -ForegroundColor Cyan

$pythonCmd = "pip"
try {
    & $pythonCmd install -e . 2>&1 | Tee-Object -FilePath "$env:TEMP\pip_install.log"
    Write-Host "✓ Dependencies berhasil diinstall" -ForegroundColor Green
} catch {
    Write-Host "✗ Error saat install dependencies: $_" -ForegroundColor Red
    Write-Host "Jalankan manual: pip install -e ." -ForegroundColor Yellow
}

# Display connection info
Write-Host "`n=== Informasi Koneksi ===" -ForegroundColor Cyan
Write-Host "Host: localhost" -ForegroundColor Green
Write-Host "Port: 5432" -ForegroundColor Green
Write-Host "Database: $dbName" -ForegroundColor Green
Write-Host "User: $newUser" -ForegroundColor Green
Write-Host "Connection String: postgresql://$newUser`:$newPassword@localhost:5432/$dbName" -ForegroundColor Green

Write-Host "`n✓ Setup PostgreSQL selesai!" -ForegroundColor Cyan
Write-Host "Langkah selanjutnya:" -ForegroundColor Yellow
Write-Host "1. Jalankan: python pertemuan6\scripts\initialize_db.py development.ini" -ForegroundColor Yellow
Write-Host "2. Jalankan server: pserve development.ini" -ForegroundColor Yellow
