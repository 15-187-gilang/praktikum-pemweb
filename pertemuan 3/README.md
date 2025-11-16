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
Prasyarat
Sebelum memulai, pastikan Anda telah menginstal:

Node.js (versi 18.x atau lebih baru direkomendasikan)
npm (biasanya terinstal bersamaan dengan Node.js)
Git
Panduan Instalasi
Clone Repository Buka terminal Anda dan clone repository ini ke komputer lokal.

git clone [URL_REPOSITORY_GIT_ANDA_DI_SINI]
Pindah ke Direktori Proyek

cd nama-folder-proyek
Instal Dependensi Jalankan perintah berikut untuk menginstal semua paket yang dibutuhkan.

npm install
Instalasi semua paket yang dibutuhkan dengan command:



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

## Laporan Testing (Screenshots Hasil Test)
<img width="1600" height="844" alt="image" src="https://github.com/user-attachments/assets/8db8752f-98d2-41fb-90ca-1aa3d2484f55" />
<img width="1600" height="841" alt="image" src="https://github.com/user-attachments/assets/5b82f6f4-0c1a-44d9-8866-f2c3ef37dd10" />



**Selamat menggunakan My Book Library! Happy Reading! 📚**
