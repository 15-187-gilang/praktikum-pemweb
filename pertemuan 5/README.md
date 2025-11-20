# Sistem Manajemen Perpustakaan Sederhana (OOP Python)

Aplikasi console sederhana untuk mengelola koleksi perpustakaan (Buku & Majalah) dengan penerapan konsep OOP yang lengkap: **Abstract Class, Inheritance, Encapsulation, Property, dan Polymorphism**.

## Fitur Utama
- Tambah item baru (Buku atau Majalah) secara interaktif  
- Tampilkan semua item (menggunakan polymorphism)  
- Cari item berdasarkan judul/kata kunci (partial & case-insensitive)  
- Validasi judul tidak boleh kosong  
- Pencegahan duplikasi ID item  
- Data demo otomatis saat pertama kali dijalankan  
- Penanganan error yang ramah pengguna  

## Konsep OOP yang Diterapkan
| Konsep          | Implementasi                                      |
|------------------|---------------------------------------------------|
| Abstract Class   | `LibraryItem` dengan `@abstractmethod`            |
| Inheritance      | `Book` dan `Magazine` → turunan `LibraryItem`     |
| Encapsulation    | Atribut private (`__author`, `__edisi`) & protected |
| Property         | Getter/setter `judul` dengan validasi             |
| Polymorphism     | `tampilkan_info()` di-override pada tiap subclass|

## Diagram Kelas (ASCII UML)
+------------------+          +-------------------+
|   LibraryItem    |<---------|       Book        |
|------------------|          |-------------------|
| _id_item: str    |          | __author: str     |
| _judul: str      |          +-------------------+
| + judul (prop)   |          | + tampilkan_info()|
| + id_item (ro)   |          +-------------------+
| + tampilkan_info()abstract     +-------------------+
+------------------+          |     Magazine      |
▲                  |-------------------|
|                  | __edisi: str      |
+------------+           +-------------------+
|   Library   |          | + tampilkan_info()|
|-------------|          +-------------------+
| __koleksi_item: List[LibraryItem] |
| + tambah_item()                    |
| + tampilkan_semua_item()           |
| + cari_item()                      |
+-------------------------------------+


## Hasil Running Program (Screenshot Text)


## Cara Menjalankan
```bash
python perpustakaan.py