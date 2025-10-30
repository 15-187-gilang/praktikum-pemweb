# penjelasan singkat
Jadwal Kuliah adalah aplikasi web sederhana berbasis HTML, CSS, dan JavaScript (ES6+) yang berfungsi untuk membantu mahasiswa mengelola jadwal kuliah harian secara   interaktif. Pengguna dapat menambahkan, mengedit, dan menghapus jadwal, serta melihat waktu saat ini secara real-time. Semua data jadwal disimpan secara permanen di localStorage, sehingga tidak hilang meskipun halaman direfresh.

# Screenshot aplikasi
<img width="1854" height="971" alt="image" src="https://github.com/user-attachments/assets/84197c96-0b11-4ab8-9975-6e278079f208" />

# Daftar fitur ES6+ yang diimplementasikan
1. let & const
   Digunakan untuk deklarasi variabel yang tidak berubah (const) dan variabel dinamis (let).
2. Arrow Functions
   Digunakan untuk fungsi renderSchedules, event listener tombol tambah, dan fungsi updateTime.
3. Template Literals
   Digunakan untuk menampilkan jadwal dalam bentuk tabel secara dinamis.
4. Class
   ScheduleManager digunakan untuk mengelola data jadwal (CRUD + localStorage).
5. Async/Await
    Diterapkan pada fungsi updateTime() untuk memperbarui jam secara real-time setiap detik.
