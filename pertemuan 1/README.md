Penjelasan Singkat Aplikasi dan Fungsi
Aplikasi Manajemen Tugas Mahasiswa adalah sebuah aplikasi client-side sederhana yang dibangun menggunakan HTML, CSS, dan JavaScript murni. Aplikasi ini dirancang untuk membantu mahasiswa dalam mengelola dan memantau aktivitas akademik mereka, khususnya daftar tugas, kuis, atau proyek. Data tugas disimpan secara lokal di peramban (browser) pengguna menggunakan fitur localStorage, sehingga data akan tetap tersimpan meskipun halaman ditutup atau di-refresh.

Screenshot Aplikasi
image Untuk membuktikan fitur Menambahkan Tugas dan Melihat Daftar Tugas. SS ini menunjukkan struktur dasar aplikasi. image Untuk membuktikan fitur Filter/Pencarian dan Perubahan Status (Selesai) serta Statistik. SS ini menunjukkan interaksi data. image Untuk membuktikan fitur Validasi Form berfungsi mencegah input data yang tidak valid.
Daftar Fitur yang Diimplementasikan
Aplikasi ini telah memenuhi semua persyaratan fitur wajib, yaitu:

Menambahkan Tugas Baru: Tugas dapat ditambahkan dengan informasi: Nama Tugas, Mata Kuliah, dan Deadline.
Manajemen Status: Pengguna dapat Menandai Selesai dan Batal Selesai untuk setiap tugas.
Hapus Tugas: Menghapus tugas yang sudah tidak diperlukan dari daftar.
Filter dan Pencarian:
Filter berdasarkan Status: Menampilkan Semua, Hanya Belum Selesai, atau Hanya Selesai.
Pencarian Teks: Pencarian real-time berdasarkan Nama Mata Kuliah.
Statistik Real-time: Menampilkan Jumlah Tugas yang Belum Selesai.
Validasi Form: Memastikan data yang dimasukkan pengguna valid.
Cara Menjalankan Aplikasi
Aplikasi ini tidak memerlukan server backend atau instalasi library/package apa pun (Zero Dependency).

Simpan File: Pastikan Anda memiliki tiga file berikut dalam satu folder yang sama:
index.html (Struktur utama)
style.css (Gaya tampilan)
script.js (Logika aplikasi)
Buka di Browser: Klik dua kali pada file index.html atau buka dengan peramban web (Chrome, Firefox, Edge, dll.).
Selesai: Aplikasi siap digunakan! Data yang Anda masukkan akan tersimpan otomatis di peramban Anda.
1. Penggunaan localStorage
Penyimpanan data diimplementasikan menggunakan Web Storage API, khususnya localStorage, sesuai petunjuk. Tugas disimpan sebagai array JavaScript Objects (arrayTasks) dan dikelola melalui langkah-langkah berikut:

Penyimpanan Data: Setiap kali ada perubahan (tambah, hapus, update status), seluruh array tugas dikonversi menjadi string JSON dan disimpan:
// Disimpan dengan key 'tasks'
localStorage.setItem('tasks', JSON.stringify(arrayTasks));
Pengambilan Data: Saat halaman dimuat (window.onload), data diambil dan dikonversi kembali menjadi array objek:
// Diambil dari key 'tasks'
arrayTasks = JSON.parse(localStorage.getItem('tasks'));
2. Validasi Form
Validasi dilakukan pada fungsi validateForm() sebelum tugas baru ditambahkan ke array:

Validasi Input Kosong: Memeriksa apakah Nama Tugas, Mata Kuliah, dan Deadline tidak kosong (.trim()). Jika ada yang kosong, pesan peringatan akan muncul.
Validasi Deadline: Memastikan tanggal yang dimasukkan tidak boleh berada di masa lalu (sudah terlewati) dibandingkan dengan tanggal hari ini. Hal ini mencegah pengguna memasukkan tugas dengan deadline yang tidak masuk akal.
Jika validasi gagal, proses penambahan tugas dihentikan (return false).
