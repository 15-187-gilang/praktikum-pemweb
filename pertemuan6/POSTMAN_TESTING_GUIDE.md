# 🧪 POSTMAN API TESTING GUIDE - Pertemuan6

## 📋 Daftar Isi
1. [Setup Postman](#setup-postman)
2. [Import Collection](#import-collection)
3. [Testing Endpoints](#testing-endpoints)
4. [Expected Results](#expected-results)
5. [Troubleshooting](#troubleshooting)

---

## 🚀 Setup Postman

### Step 1: Download Postman
- Link: https://www.postman.com/downloads/
- Download sesuai OS Anda (Windows/Mac/Linux)
- Install dan buka aplikasi

### Step 2: Login (Optional)
- Buat account Postman (atau skip)
- Login ke Postman

---

## 📥 Import Collection

### Method 1: Import File JSON (Recommended)

1. **Buka Postman**
2. **Click File → Import** (atau Ctrl+O)
3. **Pilih file:** `Pertemuan6_API.postman_collection.json`
4. **Click Import**
5. **Collection sudah siap di sidebar kiri**

### Method 2: Copy-Paste JSON

1. **Buka Postman**
2. **Click Import**
3. **Pilih tab "Raw Text"**
4. **Paste isi file JSON**
5. **Click Import**

---

## 🧪 Testing Endpoints

### ⚙️ Prerequisite
- ✅ Server Pyramid running: `pserve development.ini`
- ✅ PostgreSQL sudah connected
- ✅ Database `pertemuan6` sudah dibuat

### 📝 Endpoint List

| No | Method | Endpoint | Deskripsi |
|----|--------|----------|-----------|
| 1 | GET | `/api/models` | Ambil semua matakuliah |
| 2 | GET | `/api/models/{id}` | Ambil detail matakuliah |
| 3 | POST | `/api/models` | Tambah matakuliah baru |
| 4 | PUT | `/api/models/{id}` | Update matakuliah |
| 5 | DELETE | `/api/models/{id}` | Hapus matakuliah |

---

## 🎯 Testing Step-by-Step

### 1️⃣ TEST GET - Daftar Semua Matakuliah

**URL:** `http://localhost:6543/api/models`  
**Method:** `GET`

**Steps:**
1. Click request "GET - Daftar Semua Matakuliah"
2. Click **Send**
3. Lihat response di bawah

**Expected Response (Status 200):**
```json
{
  "success": true,
  "message": "Berhasil mengambil 0 data",
  "data": [],
  "total": 0
}
```

*(Awalnya data kosong, akan berisi data setelah POST)*

---

### 2️⃣ TEST POST - Tambah Data Baru

**URL:** `http://localhost:6543/api/models`  
**Method:** `POST`  
**Body:**
```json
{
  "name": "Algoritma dan Pemrograman",
  "value": 3
}
```

**Steps:**
1. Click request "POST - Tambah Matakuliah Baru"
2. Di **Body**, pastikan JSON terisi:
   ```json
   {
     "name": "Algoritma dan Pemrograman",
     "value": 3
   }
   ```
3. Click **Send**

**Expected Response (Status 201):**
```json
{
  "success": true,
  "message": "Data berhasil ditambahkan",
  "data": {
    "id": 1,
    "name": "Algoritma dan Pemrograman",
    "value": 3
  }
}
```

---

### 3️⃣ TEST POST - Tambah Data Kedua

Ulangi Step 2 dengan data berbeda:

**Body:**
```json
{
  "name": "Struktur Data",
  "value": 4
}
```

**Expected:** Status 201, ID akan menjadi 2

---

### 4️⃣ TEST GET - Daftar Semua (Lihat Data yang Ditambah)

**URL:** `http://localhost:6543/api/models`  
**Method:** `GET`

**Steps:**
1. Click "GET - Daftar Semua Matakuliah"
2. Click **Send**

**Expected Response (Status 200):**
```json
{
  "success": true,
  "message": "Berhasil mengambil 2 data",
  "data": [
    {
      "id": 1,
      "name": "Algoritma dan Pemrograman",
      "value": 3
    },
    {
      "id": 2,
      "name": "Struktur Data",
      "value": 4
    }
  ],
  "total": 2
}
```

---

### 5️⃣ TEST GET - Detail Satu Data

**URL:** `http://localhost:6543/api/models/1`  
**Method:** `GET`

**Steps:**
1. Click "GET - Detail Matakuliah (by ID)"
2. URL: ubah `1` ke ID yang ingin dilihat
3. Click **Send**

**Expected Response (Status 200):**
```json
{
  "success": true,
  "message": "Data berhasil diambil",
  "data": {
    "id": 1,
    "name": "Algoritma dan Pemrograman",
    "value": 3
  }
}
```

---

### 6️⃣ TEST PUT - Update Data

**URL:** `http://localhost:6543/api/models/1`  
**Method:** `PUT`  
**Body:**
```json
{
  "name": "Algoritma dan Pemrograman (Lanjutan)",
  "value": 4
}
```

**Steps:**
1. Click "PUT - Update Matakuliah"
2. URL: ubah ID sesuai yang ingin diupdate
3. Di **Body**, update data:
   ```json
   {
     "name": "Algoritma dan Pemrograman (Lanjutan)",
     "value": 4
   }
   ```
4. Click **Send**

**Expected Response (Status 200):**
```json
{
  "success": true,
  "message": "Data berhasil diupdate",
  "data": {
    "id": 1,
    "name": "Algoritma dan Pemrograman (Lanjutan)",
    "value": 4
  }
}
```

---

### 7️⃣ TEST DELETE - Hapus Data

**URL:** `http://localhost:6543/api/models/1`  
**Method:** `DELETE`

**Steps:**
1. Click "DELETE - Hapus Matakuliah"
2. URL: ubah ID sesuai yang ingin dihapus
3. Click **Send**

**Expected Response (Status 200):**
```json
{
  "success": true,
  "message": "Data dengan ID 1 berhasil dihapus"
}
```

---

### 8️⃣ VERIFY DELETE - GET untuk Confirm

Jalankan GET semua data lagi untuk memastikan data sudah dihapus:

**URL:** `http://localhost:6543/api/models`

**Expected:** Data yang dihapus sudah tidak ada

---

## 📊 Expected Results Summary

| Test | Method | Status | Hasil |
|------|--------|--------|-------|
| 1. GET All (Awal) | GET | 200 | Data kosong |
| 2. POST Data 1 | POST | 201 | ID 1 created |
| 3. POST Data 2 | POST | 201 | ID 2 created |
| 4. GET All | GET | 200 | 2 data |
| 5. GET Detail | GET | 200 | 1 data |
| 6. PUT Update | PUT | 200 | Data updated |
| 7. DELETE | DELETE | 200 | Data deleted |
| 8. GET All (Final) | GET | 200 | 1 data |

---

## 🔴 Error Responses

### ❌ 404 - Not Found
```json
{
  "success": false,
  "message": "Data dengan ID 999 tidak ditemukan",
  "data": null
}
```
**Penyebab:** ID tidak ada di database

### ❌ 400 - Bad Request
```json
{
  "success": false,
  "message": "Field \"name\" dan \"value\" wajib diisi"
}
```
**Penyebab:** Data POST/PUT tidak lengkap

### ❌ 500 - Server Error
```json
{
  "success": false,
  "message": "Error: ..."
}
```
**Penyebab:** Error di server

---

## 🛠️ Troubleshooting

### Problem: "Connection refused"
**Solution:**
- Pastikan server running: `pserve development.ini`
- Pastikan port 6543 tidak digunakan aplikasi lain
- Try: `netstat -ano | findstr :6543`

### Problem: "404 Not Found"
**Solution:**
- Cek URL endpoint benar
- Cek method (GET/POST/PUT/DELETE) benar
- Cek ID yang digunakan sudah exist

### Problem: "Database connection error"
**Solution:**
- Pastikan PostgreSQL running
- Cek connection string di `development.ini`
- Run: `python check_db.py`

### Problem: "JSON parse error"
**Solution:**
- Pastikan Body format JSON benar
- Check Content-Type: `application/json`
- Gunakan JSON validator: https://jsonlint.com/

---

## 📈 Tips & Tricks

### 1. Use Variables
Postman punya variables untuk tidak perlu retype URL:

```
{{base_url}}/api/models    → http://localhost:6543/api/models
{{model_id}}               → 1
```

Pre-configured di collection, tinggal pakai!

### 2. Save Request Response
1. After send, click **Save** di response
2. Pilih folder untuk save
3. Later, bisa lihat history responses

### 3. Run Collection (Test Multiple)
1. Click folder "Matakuliah"
2. Click **Run** (play icon)
3. Akan run semua request in sequence

### 4. Export Results
1. Setelah Run Collection
2. Click **Export Results**
3. Save as JSON atau CSV

---

## 📚 API Documentation

### Base URL
```
http://localhost:6543
```

### Models Resource
- **Description:** Manajemen data matakuliah
- **Base Path:** `/api/models`

### Field Types
- **id:** Integer (auto-increment)
- **name:** String (max 255)
- **value:** Integer

### Response Format
```json
{
  "success": boolean,
  "message": string,
  "data": object | array | null,
  "total": number (optional)
}
```

---

## ✅ Full Testing Checklist

Pastikan semua sudah di-test:

- [ ] GET all data (empty)
- [ ] POST data 1
- [ ] POST data 2
- [ ] GET all data (2 results)
- [ ] GET detail by ID
- [ ] PUT update data
- [ ] DELETE data
- [ ] GET all (verify delete)
- [ ] Test error cases (invalid ID)
- [ ] Test validation (missing fields)

---

## 🎯 Next Steps

1. ✅ Import collection ke Postman
2. ✅ Test semua endpoints
3. ✅ Verify database changes
4. ✅ Check response status codes
5. ✅ Document any issues

---

## 📞 Support

**Jika ada masalah:**
1. Check server logs: `pserve development.ini` output
2. Check database: `python check_db.py`
3. Check Postman console: View → Show Postman Console
4. Check request/response bodies

---

**Happy Testing! 🎉**

File: `Pertemuan6_API.postman_collection.json`
