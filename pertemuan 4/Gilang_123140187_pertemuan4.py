# Program Pengelolaan Data Nilai Mahasiswa
# Menggunakan list of dictionary

# Inisialisasi data awal (minimal 5 mahasiswa)
mahasiswa_list = [
    {"nama": "tengku", "nim": "1230140040", "nilai_uts": 85, "nilai_uas": 78, "nilai_tugas": 90},
    {"nama": "ripaldy", "nim": "1230140123", "nilai_uts": 70, "nilai_uas": 75, "nilai_tugas": 80},
    {"nama": "ridho", "nim": "123140197", "nilai_uts": 60, "nilai_uas": 65, "nilai_tugas": 70},
    {"nama": "max", "nim": "123140191", "nilai_uts": 45, "nilai_uas": 50, "nilai_tugas": 55},
    {"nama": "ihsan", "nim": "123140011", "nilai_uts": 95, "nilai_uas": 90, "nilai_tugas": 88}
]

# Fungsi 1: Hitung nilai akhir
def hitung_nilai_akhir(uts, uas, tugas):
    return 0.3 * uts + 0.4 * uas + 0.3 * tugas

# Fungsi 2: Tentukan grade
def tentukan_grade(nilai_akhir):
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"

# Fungsi 3: Tampilkan data dalam tabel
def tampilkan_tabel(data):
    print("\n" + "="*110)
    print(f"{'No':<3} {'Nama':<12} {'NIM':<8} {'UTS':<6} {'UAS':<6} {'Tugas':<6} {'Nilai Akhir':<12} {'Grade':<6}")
    print("="*110)
    for i, mhs in enumerate(data, 1):
        nilai_akhir = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        grade = tentukan_grade(nilai_akhir)
        print(f"{i:<3} {mhs['nama']:<12} {mhs['nim']:<8} {mhs['nilai_uts']:<6} {mhs['nilai_uas']:<6} {mhs['nilai_tugas']:<6} {nilai_akhir:<12.2f} {grade:<6}")
    print("="*110)

# Fungsi 4: Cari mahasiswa dengan nilai tertinggi dan terendah
def cari_nilai_ekstrem(data):
    if not data:
        return None, None
    
    # Hitung nilai akhir untuk semua
    for mhs in data:
        mhs['nilai_akhir'] = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
    
    tertinggi = max(data, key=lambda x: x['nilai_akhir'])
    terendah = min(data, key=lambda x: x['nilai_akhir'])
    
    return tertinggi, terendah

# Fungsi Tambahan 1: Input data mahasiswa baru
def tambah_mahasiswa():
    print("\n--- Tambah Mahasiswa Baru ---")
    nama = input("Nama: ").strip()
    nim = input("NIM: ").strip()
    
    # Validasi input nilai
    while True:
        try:
            uts = int(input("Nilai UTS: "))
            uas = int(input("Nilai UAS: "))
            tugas = int(input("Nilai Tugas: "))
            if all(0 <= n <= 100 for n in [uts, uas, tugas]):
                break
            else:
                print("Nilai harus antara 0 dan 100!")
        except ValueError:
            print("Masukkan angka yang valid!")
    
    mahasiswa_baru = {
        "nama": nama,
        "nim": nim,
        "nilai_uts": uts,
        "nilai_uas": uas,
        "nilai_tugas": tugas
    }
    mahasiswa_list.append(mahasiswa_baru)
    print(f"Mahasiswa {nama} berhasil ditambahkan!")

# Fungsi Tambahan 2: Filter berdasarkan grade
def filter_berdasarkan_grade(data, grade_target):
    hasil = []
    for mhs in data:
        na = hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas'])
        if tentukan_grade(na) == grade_target.upper():
            mhs_copy = mhs.copy()
            mhs_copy['nilai_akhir'] = na
            mhs_copy['grade'] = grade_target.upper()
            hasil.append(mhs_copy)
    return hasil

# Fungsi Tambahan 3: Hitung rata-rata nilai kelas
def hitung_rata_rata_kelas(data):
    if not data:
        return 0
    total = sum(hitung_nilai_akhir(mhs['nilai_uts'], mhs['nilai_uas'], mhs['nilai_tugas']) for mhs in data)
    return total / len(data)

# Menu Utama
def menu():
    while True:
        print("\n" + "="*50)
        print("   PROGRAM PENGELOLAAN NILAI MAHASISWA")
        print("="*50)
        print("1. Tampilkan Semua Data")
        print("2. Tambah Mahasiswa Baru")
        print("3. Cari Nilai Tertinggi & Terendah")
        print("4. Filter Berdasarkan Grade")
        print("5. Hitung Rata-rata Kelas")
        print("6. Keluar")
        print("="*50)
        
        pilihan = input("Pilih menu (1-6): ").strip()
        
        if pilihan == "1":
            tampilkan_tabel(mahasiswa_list)
        
        elif pilihan == "2":
            tambah_mahasiswa()
        
        elif pilihan == "3":
            tertinggi, terendah = cari_nilai_ekstrem(mahasiswa_list)
            if tertinggi and terendah:
                print("\n--- NILAI TERTINGGI ---")
                print(f"Nama: {tertinggi['nama']}, NIM: {tertinggi['nim']}, Nilai Akhir: {tertinggi['nilai_akhir']:.2f}")
                print("--- NILAI TERENDAH ---")
                print(f"Nama: {terendah['nama']}, NIM: {terendah['nim']}, Nilai Akhir: {terendah['nilai_akhir']:.2f}")
        
        elif pilihan == "4":
            grade = input("Masukkan grade yang ingin difilter (A/B/C/D/E): ").strip().upper()
            if grade in ['A','B','C','D','E']:
                hasil = filter_berdasarkan_grade(mahasiswa_list, grade)
                if hasil:
                    print(f"\nMahasiswa dengan Grade {grade}:")
                    tampilkan_tabel(hasil)
                else:
                    print(f"Tidak ada mahasiswa dengan grade {grade}.")
            else:
                print("Grade tidak valid!")
        
        elif pilihan == "5":
            rata = hitung_rata_rata_kelas(mahasiswa_list)
            print(f"\nRata-rata nilai kelas: {rata:.2f}")
        
        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break
        
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

# Jalankan program
if __name__ == "__main__":
    menu()