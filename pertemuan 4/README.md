# Program Pengelolaan Nilai Mahasiswa

Sebuah aplikasi sederhana berbasis Python untuk mengelola data nilai mahasiswa, menghitung nilai akhir, menentukan grade, serta menyajikan berbagai fitur analisis seperti pencarian nilai tertinggi/terendah, filtering berdasarkan grade, dan rata-rata kelas.

## Fitur Utama

- Menampilkan seluruh data mahasiswa dalam bentuk tabel rapi  
- Menambahkan data mahasiswa baru dengan validasi input  
- Menghitung nilai akhir otomatis (30% UTS + 40% UAS + 30% Tugas)  
- Menentukan grade (A, B, C, D, E) berdasarkan nilai akhir  
- Mencari mahasiswa dengan nilai tertinggi dan terendah  
- Filter mahasiswa berdasarkan grade tertentu  
- Menghitung rata-rata nilai akhir seluruh kelas  
- Antarmuka menu interaktif yang mudah digunakan  

## Bobot Penilaian

| Komponen       | Persentase |
|----------------|------------|
| Nilai UTS      | 30%        |
| Nilai UAS      | 40%        |
| Nilai Tugas    | 30%        |

## Rentang Grade

| Nilai Akhir    | Grade |
|----------------|-------|
| ≥ 80           | A     |
| ≥ 70 - < 80    | B     |
| ≥ 60 - < 70    | C     |
| ≥ 50 - < 60    | D     |
| < 50           | E     |

## hasil screenshot

## Cara Menjalankan Program

1. Pastikan Anda memiliki **Python 3** terinstal di komputer.
2. Simpan kode ke file bernama `nilai_mahasiswa.py` (atau nama lain sesuai keinginan).
3. Buka terminal/command prompt.
4. Jalankan perintah:

```bash
python nilai_mahasiswa.py
