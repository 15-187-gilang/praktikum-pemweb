# Penjelasan Singkat Aplikasi dan Fungsi
Aplikasi Manajemen Tugas Mahasiswa adalah sebuah aplikasi **client-side** sederhana yang dibangun menggunakan **HTML, CSS, dan JavaScript murni**. Aplikasi ini dirancang untuk membantu mahasiswa dalam **mengelola dan memantau aktivitas akademik** mereka, khususnya daftar tugas, kuis, atau proyek. Data tugas disimpan secara **lokal di peramban (browser)** pengguna menggunakan fitur **`localStorage`**, sehingga data akan tetap tersimpan meskipun halaman ditutup atau di-refresh.

#  Screenshot Aplikasi
<img width="1003" height="452" alt="image" src="https://github.com/user-attachments/assets/6c2540d6-3d6a-4eff-9389-f283b70630c6" />
Untuk membuktikan fitur Menambahkan Tugas dan Melihat Daftar Tugas. SS ini menunjukkan struktur dasar aplikasi.
<img width="1023" height="333" alt="image" src="https://github.com/user-attachments/assets/62ac03de-aed0-41a9-9a50-474b09176541" />
Untuk membuktikan fitur Filter/Pencarian dan Perubahan Status (Selesai) serta Statistik. SS ini menunjukkan interaksi data.
<img width="996" height="659" alt="image" src="https://github.com/user-attachments/assets/ef13b0b9-5970-4c28-9056-50538af98724" />
Untuk membuktikan fitur Validasi Form berfungsi mencegah input data yang tidak valid.

# Daftar Fitur yang Diimplementasikan
Aplikasi ini telah memenuhi semua persyaratan fitur wajib, yaitu:

1.  **Menambahkan Tugas Baru**: Tugas dapat ditambahkan dengan informasi: **Nama Tugas**, **Mata Kuliah**, dan **Deadline**.
2.  **Manajemen Status**: Pengguna dapat **Menandai Selesai** dan **Batal Selesai** untuk setiap tugas.
3.  **Hapus Tugas**: Menghapus tugas yang sudah tidak diperlukan dari daftar.
4.  **Filter dan Pencarian**:
    * **Filter berdasarkan Status**: Menampilkan Semua, Hanya Belum Selesai, atau Hanya Selesai.
    * **Pencarian Teks**: Pencarian real-time berdasarkan **Nama Mata Kuliah**.
5.  **Statistik Real-time**: Menampilkan **Jumlah Tugas yang Belum Selesai**.
6.  **Validasi Form**: Memastikan data yang dimasukkan pengguna valid.

# Cara Menjalankan Aplikasi

Aplikasi ini tidak memerlukan server backend atau instalasi library/package apa pun (Zero Dependency).

1.  **Simpan File**: Pastikan Anda memiliki tiga file berikut dalam satu folder yang sama:
    * `index.html` (Struktur utama)
    * `style.css` (Gaya tampilan)
    * `script.js` (Logika aplikasi)
2.  **Buka di Browser**: Klik dua kali pada file **`index.html`** atau buka dengan peramban web (Chrome, Firefox, Edge, dll.).
3.  **Selesai**: Aplikasi siap digunakan! Data yang Anda masukkan akan tersimpan otomatis di peramban Anda.

## 1. Penggunaan `localStorage`

Penyimpanan data diimplementasikan menggunakan Web Storage API, khususnya `localStorage`, sesuai petunjuk. Tugas disimpan sebagai array JavaScript Objects (`arrayTasks`) dan dikelola melalui langkah-langkah berikut:

* **Penyimpanan Data**: Setiap kali ada perubahan (tambah, hapus, update status), seluruh array tugas dikonversi menjadi string JSON dan disimpan:
    ```javascript
    // Disimpan dengan key 'tasks'
    localStorage.setItem('tasks', JSON.stringify(arrayTasks));
    ```
* **Pengambilan Data**: Saat halaman dimuat (`window.onload`), data diambil dan dikonversi kembali menjadi array objek:
    ```javascript
    // Diambil dari key 'tasks'
    arrayTasks = JSON.parse(localStorage.getItem('tasks'));
    ```

## 2. Validasi Form

Validasi dilakukan pada fungsi `validateForm()` sebelum tugas baru ditambahkan ke array:

* **Validasi Input Kosong**: Memeriksa apakah **Nama Tugas**, **Mata Kuliah**, dan **Deadline** tidak kosong (`.trim()`). Jika ada yang kosong, pesan peringatan akan muncul.
* **Validasi Deadline**: Memastikan tanggal yang dimasukkan **tidak boleh berada di masa lalu** (sudah terlewati) dibandingkan dengan tanggal hari ini. Hal ini mencegah pengguna memasukkan tugas dengan deadline yang tidak masuk akal.

Jika validasi gagal, proses penambahan tugas dihentikan (`return false`).
