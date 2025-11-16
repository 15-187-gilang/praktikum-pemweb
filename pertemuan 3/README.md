# 📚 My Book Library

Aplikasi manajemen koleksi buku pribadi yang dibuat dengan Next.js dan React. Kelola, cari, dan analisis koleksi buku Anda dengan mudah dan interaktif.

## Deskripsi Aplikasi

My Book Library adalah aplikasi web modern yang dirancang untuk membantu Anda mengelola koleksi buku pribadi. Dengan antarmuka yang intuitif dan responsif, Anda dapat dengan mudah menambahkan buku baru, mencari buku yang sudah dimiliki, memfilter berdasarkan status, dan melihat statistik lengkap koleksi Anda. Data disimpan secara lokal di browser sehingga tidak perlu koneksi internet untuk mengakses koleksi Anda.

## ✨ Fitur Utama

- **CRUD Operations Lengkap**: Tambah, edit, hapus buku dengan mudah
- **Pencarian Real-time**: Cari buku berdasarkan judul atau nama penulis
- **Sistem Filter**: Filter buku berdasarkan status (Dibaca, Sedang Dibaca, Ingin Dibaca)
- **Statistik & Analytics**: Lihat ringkasan dan grafik distribusi koleksi
- **Penyimpanan Lokal**: Data tersimpan otomatis di localStorage
- **Responsive Design**: Bekerja sempurna di desktop, tablet, dan mobile
- **Validasi Form**: Input validation untuk memastikan data yang benar
- **Animasi Smooth**: Transisi halus dan user experience yang menyenangkan

## 🛠️ Teknologi yang Digunakan

- **Next.js 16** - Framework React dengan Turbopack
- **React 19.2** - Library UI terbaru
- **CSS3** - Styling dengan gradient, animasi, dan responsive design
- **Context API** - State management global
- **React Hooks** - useState, useEffect, useContext untuk logic komponen
- **localStorage** - Persistensi data di browser
- **vaul** - UI component library

## Instruksi Instalasi dan Menjalankan

### Prasyarat

Sebelum memulai, pastikan Anda sudah menginstal:

- **Node.js** (versi 18 atau lebih baru direkomendasikan) - [Download di sini](https://nodejs.org/)
- **npm** (bersama dengan Node.js)
- **Git** (opsional, untuk clone repository)

### Panduan Instalasi

#### 1. Clone Repository

Buka terminal Anda dan clone repository ini ke komputer lokal:

\`\`\`bash
git clone [URL_REPOSITORY_GET_ANDA_DI_SINI]
\`\`\`

Atau jika menggunakan file ZIP, extract terlebih dahulu ke folder yang diinginkan.

#### 2. Pindah ke Direktori Proyek

\`\`\`bash
cd personal-book-app
\`\`\`

atau ganti dengan nama folder Anda.

#### 3. Instal Dependensi Jalankan Perintah Berikut

Instalasi semua paket yang dibutuhkan dengan command:

\`\`\`bash
npm install --legacy-peer-deps
\`\`\`

Perintah ini akan mengunduh dan menginstal semua paket yang tercantum dalam `package.json`. Termasuk:

**Dependencies (Untuk Produksi):**
- **react & react-dom** - Library UI terbaru dengan React 19
- **next** - Framework Next.js 16 dengan Turbopack
- **vaul** - UI component library

**DevDependencies (Untuk Pengembangan & Testing):**
- **turbopack** - Build tool server pengembangan yang super cepat
- **eslint** - Untuk analisis kode statis
- **jest & testing-library/react** - Framework testing dan transpiler

---

## Menjalankan Aplikasi

### Untuk Menjalankan Server Pengembangan:

\`\`\`bash
npm run dev
\`\`\`

Aplikasi akan tersedia dan dapat diakses melalui: **http://localhost:3000**

### Untuk Menjalankan Pengujian (Unit Test):

\`\`\`bash
npm test
\`\`\`

---

## Screenshot Antarmuka

### Halaman Home
- **Header dengan Logo** - Judul aplikasi dan tombol navigasi
- **Search Bar** - Cari buku berdasarkan judul atau penulis
- **Filter Dropdown** - Filter berdasarkan status buku
- **Book Form** - Form untuk menambah atau edit buku
- **Book List** - Daftar buku dengan kartu interaktif
- **Action Buttons** - Tombol Edit dan Hapus untuk setiap buku

### Halaman Statistik
- **Total Books Counter** - Jumlah total buku di koleksi
- **Status Distribution Chart** - Grafik pie chart distribusi status
- **Books Table** - Tabel lengkap semua buku
- **Back Button** - Navigasi kembali ke halaman home

---

## 📚 Penjelasan Fitur React yang Digunakan

### 1. Context API untuk State Management
Mengelola state global sehingga data dapat diakses dari semua komponen tanpa prop drilling.

\`\`\`jsx
// BookContext.jsx - Centralized state management
const BookContext = createContext();
export const BookProvider = ({ children }) => {
  const [books, setBooks] = useLocalStorage('books', []);
  // Semua operasi CRUD di sini
};
\`\`\`

### 2. Custom Hooks

#### useLocalStorage
Hook untuk sinkronisasi otomatis state dengan localStorage.

\`\`\`jsx
const [books, setBooks] = useLocalStorage('books', []);
// State otomatis disimpan ke localStorage
\`\`\`

#### useBookStats
Hook untuk menghitung statistik koleksi buku.

\`\`\`jsx
const stats = useBookStats();
// { total: 10, dibaca: 5, sedangDibaca: 3, inginDibaca: 2 }
\`\`\`

### 3. React Hooks
- **useState** - Mengelola state lokal komponen
- **useEffect** - Side effects dan sinkronisasi data
- **useContext** - Mengakses data global dari Context

### 4. Komponen Reusable
- `Home` - Halaman utama dengan CRUD dan filter
- `Stats` - Halaman statistik dengan grafik
- `BookForm` - Form tambah/edit buku
- `BookList` - Daftar buku
- `BookItem` - Card individual buku
- `BookFilter` - Filter dropdown
- `SearchBar` - Komponen pencarian

---

## 📁 Struktur Folder

\`\`\`
personal-book-app/
├── app/
│   ├── page.tsx                    # Halaman utama
│   ├── layout.tsx                  # Layout global
│   ├── globals.css                 # Styling global
│   ├── lib/
│   │   ├── context/
│   │   │   └── BookContext.jsx     # State management
│   │   └── hooks/
│   │       ├── useLocalStorage.js  # Custom hook storage
│   │       └── useBookStats.js     # Custom hook statistik
│   └── components/
│       ├── pages/
│       │   ├── Home.jsx            # Halaman Home
│       │   ├── Home.css
│       │   ├── Stats.jsx           # Halaman Statistik
│       │   └── Stats.css
│       ├── BookForm/
│       │   ├── BookForm.jsx
│       │   └── BookForm.css
│       ├── BookList/
│       │   ├── BookList.jsx
│       │   └── BookList.css
│       ├── BookItem/
│       │   ├── BookItem.jsx
│       │   └── BookItem.css
│       ├── BookFilter/
│       │   ├── BookFilter.jsx
│       │   └── BookFilter.css
│       └── SearchBar/
│           ├── SearchBar.jsx
│           └── SearchBar.css
├── public/                         # File statis (logo, gambar)
├── package.json                    # Dependencies
├── next.config.js                  # Konfigurasi Next.js
└── README.md                       # Dokumentasi
\`\`\`

---

## 🎮 Cara Menggunakan Aplikasi

### Menambah Buku
1. Isi form input dengan judul, penulis, genre, dan status
2. Klik tombol "Tambah Buku"
3. Buku langsung muncul di daftar dan tersimpan otomatis

### Mencari Buku
1. Ketik judul atau nama penulis di search bar
2. Daftar akan terupdate secara real-time

### Filter Berdasarkan Status
1. Klik dropdown filter
2. Pilih status yang ingin dilihat
3. Daftar hanya menampilkan buku dengan status tersebut

### Edit Buku
1. Klik tombol "Edit" pada buku yang ingin diubah
2. Form akan terisi otomatis dengan data buku
3. Ubah data yang diinginkan
4. Klik "Update Buku" untuk menyimpan

### Hapus Buku
1. Klik tombol "Hapus" pada buku yang ingin dihapus
2. Konfirmasi penghapusan
3. Buku akan dihapus dari koleksi

### Lihat Statistik
1. Klik tab "Lihat Statistik" di header
2. Tampilkan statistik lengkap dan grafik distribusi koleksi Anda

---

## ⚙️ Command-Command Penting

| Command | Fungsi |
|---------|--------|
| `npm run dev` | Jalankan mode development |
| `npm run build` | Build untuk production |
| `npm run start` | Jalankan build production |
| `npm run lint` | Check code quality |
| `npm test` | Jalankan pengujian unit |
| `Ctrl + C` | Stop server (Windows/Mac) |

---

## Laporan Testing (Screenshots Hasil Test)

Pengujian unit dilakukan menggunakan Jest dan React Testing Library untuk memverifikasi fungsionalitas komponen dan logika bisnis. Terdapat total 5 skenario pengujian yang telah dibuat.

### Hasil Pengujian

- **Screenshot di bawah ini menunjukkan bahwa kelima skenario pengujian berhasil dijalankan tanpa ada yang gagal.**

#### Skenario Pengujian:

1. **Test: Render Home Component**
   - Memverifikasi bahwa komponen Home dapat dirender dengan benar
   - Hasil: ✅ PASS

2. **Test: Add Book Functionality**
   - Menguji fungsi penambahan buku baru
   - Memasukkan data buku dan memverifikasi buku muncul di daftar
   - Hasil: ✅ PASS

3. **Test: Edit Book Functionality**
   - Menguji fungsi edit/update buku
   - Mengubah data buku dan memverifikasi perubahan tersimpan
   - Hasil: ✅ PASS

4. **Test: Delete Book Functionality**
   - Menguji fungsi penghapusan buku
   - Menghapus buku dan memverifikasi buku hilang dari daftar
   - Hasil: ✅ PASS

5. **Test: Filter and Search Functionality**
   - Menguji fitur pencarian dan filter berdasarkan status
   - Memverifikasi bahwa daftar buku tersaring dengan benar
   - Hasil: ✅ PASS

### Menjalankan Test

Untuk menjalankan semua test, gunakan command:

\`\`\`bash
npm test
\`\`\`

Untuk menjalankan test dalam mode watch (auto-refresh saat ada perubahan):

\`\`\`bash
npm test -- --watch
\`\`\`

Untuk melihat coverage laporan:

\`\`\`bash
npm test -- --coverage
\`\`\`

---

## 🔧 Troubleshooting

### Error: "Port 3000 already in use"
Gunakan port alternatif:
\`\`\`bash
npm run dev -- -p 3001
\`\`\`

### Error: "ERESOLVE unable to resolve dependency tree"
Gunakan flag legacy-peer-deps:
\`\`\`bash
npm install --legacy-peer-deps
npm run dev
\`\`\`

### Error: "Module not found"
Install ulang dependencies:
\`\`\`bash
rm -r node_modules package-lock.json
npm install --legacy-peer-deps
\`\`\`

### Data tidak tersimpan setelah refresh
- Periksa pengaturan privacy browser (allow localStorage)
- Bersihkan cache browser (Ctrl + Shift + Delete)
- Refresh halaman (F5 atau Ctrl + Shift + R untuk hard refresh)

### Aplikasi tidak load
- Pastikan terminal menampilkan "Ready in..."
- Refresh browser (F5)
- Tutup dan buka ulang terminal, jalankan `npm run dev` lagi

---

## 💡 Tips & Tricks

- **Local Development**: Data tersimpan per browser, pastikan gunakan browser yang sama
- **Mobile Testing**: Aplikasi responsif, bisa diakses dari smartphone
- **Backup Data**: Export koleksi secara berkala jika diperlukan
- **Privacy**: Semua data disimpan lokal, tidak ada upload ke server

---

**Selamat menggunakan My Book Library! Happy Reading! 📚**
