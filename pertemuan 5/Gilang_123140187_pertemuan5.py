"""Sistem Manajemen Perpustakaan Sederhana

Modul ini berisi implementasi sistem manajemen perpustakaan sederhana
menggunakan konsep OOP: Abstract Class, Inheritance, Encapsulation,
Property, dan Polymorphism.
"""

from abc import ABC, abstractmethod
from typing import List, Optional

# ========================================
# Kelas Dasar (LibraryItem) dan Subkelas (Book, Magazine)
# (Tidak diubah, karena sudah benar)
# ========================================

class LibraryItem(ABC):
    """
    Abstract base class untuk semua item perpustakaan.
    """

    def __init__(self, id_item: str, judul: str):
        self._id_item = id_item
        self.judul = judul 

    @property
    def judul(self) -> str:
        """Getter untuk atribut judul."""
        return self._judul

    @judul.setter
    def judul(self, nilai: str):
        """Setter untuk judul dengan validasi."""
        if not nilai or nilai.strip() == "":
            raise ValueError("Judul tidak boleh kosong!")
        self._judul = nilai.strip()

    @property
    def id_item(self) -> str:
        """Getter untuk ID item (read-only)."""
        return self._id_item

    @abstractmethod
    def tampilkan_info(self):
        """
        Method abstract yang harus diimplementasikan oleh subclass.
        Menampilkan informasi lengkap item.
        """
        pass


class Book(LibraryItem):
    """Kelas untuk item jenis Buku, mewarisi dari LibraryItem."""
    def __init__(self, id_item: str, judul: str, author: str):
        super().__init__(id_item, judul)
        self.__author = author

    @property
    def author(self) -> str:
        """Getter untuk penulis."""
        return self.__author

    def tampilkan_info(self):
        """Menampilkan informasi lengkap buku."""
        print(f"[Buku] ID: {self.id_item} | Judul: {self.judul} | Penulis: {self.__author}")


class Magazine(LibraryItem):
    """Kelas untuk item jenis Majalah, mewarisi dari LibraryItem."""
    def __init__(self, id_item: str, judul: str, edisi: str):
        super().__init__(id_item, judul)
        self.__edisi = edisi

    @property
    def edisi(self) -> str:
        """Getter untuk edisi."""
        return self.__edisi

    def tampilkan_info(self):
        """Menampilkan informasi lengkap majalah."""
        print(f"[Majalah] ID: {self.id_item} | Judul: {self.judul} | Edisi: {self.__edisi}")


class Library:
    """Kelas pengelola koleksi item perpustakaan."""
    def __init__(self):
        self.__koleksi_item: List[LibraryItem] = []

    def tambah_item(self, item: LibraryItem):
        """Menambahkan item ke koleksi."""
        if not isinstance(item, LibraryItem):
            raise TypeError("Item harus berupa turunan dari LibraryItem")
        # Cek duplikasi ID
        if any(i.id_item == item.id_item for i in self.__koleksi_item):
            print(f"ERROR: Item dengan ID {item.id_item} sudah ada di koleksi.")
            return

        self.__koleksi_item.append(item)
        print(f"Item '{item.judul}' (ID: {item.id_item}) berhasil ditambahkan.")

    def tampilkan_semua_item(self):
        """Menampilkan semua item di koleksi (polymorphism)."""
        if not self.__koleksi_item:
            print("Koleksi perpustakaan kosong.")
            return

        print("\n=== DAFTAR SEMUA ITEM PERPUSTAKAAN ===")
        for item in self.__koleksi_item:
            item.tampilkan_info()
        print("=" * 42)

    def cari_item(self, judul: str) -> Optional[LibraryItem]:
        """Mencari item berdasarkan judul (case-insensitive partial match)."""
        judul_lower = judul.strip().lower()
        hasil = [
            item for item in self.__koleksi_item
            if judul_lower in item.judul.lower()
        ]

        if not hasil:
            print(f"Item dengan judul mengandung '{judul}' tidak ditemukan.")
            return None

        print(f"\nDitemukan {len(hasil)} item dengan judul mengandung '{judul}':")
        for item in hasil:
            item.tampilkan_info()
        # Mengembalikan list hasil
        return hasil


# ========================================
# Fungsi Interaktif untuk Input Pengguna
# ========================================

def tambah_item_interaktif(perpustakaan: Library):
    """Meminta input dari pengguna dan menambahkan item ke perpustakaan."""
    print("\n--- TAMBAH ITEM BARU ---")
    
    # Memilih jenis item
    while True:
        jenis = input("Jenis Item (B/M - Buku/Majalah): ").strip().upper()
        if jenis in ['B', 'M']:
            break
        print("Pilihan tidak valid. Masukkan 'B' untuk Buku atau 'M' untuk Majalah.")

    # Input data umum
    id_item = input("Masukkan ID Item (misal: B003): ").strip()
    
    # Mencegah Judul kosong (pengecualian akan ditangani di LibraryItem)
    while True:
        try:
            judul = input("Masukkan Judul Item: ").strip()
            if not judul:
                raise ValueError
            break
        except ValueError:
            print("Judul tidak boleh kosong. Coba lagi.")

    try:
        if jenis == 'B':
            # Input data khusus Buku
            author = input("Masukkan Nama Penulis: ").strip()
            item_baru = Book(id_item, judul, author)
        
        elif jenis == 'M':
            # Input data khusus Majalah
            edisi = input("Masukkan Edisi Majalah (misal: Vol. 1): ").strip()
            item_baru = Magazine(id_item, judul, edisi)
        
        # Tambahkan item ke koleksi
        perpustakaan.tambah_item(item_baru)
        
    except ValueError as e:
        print(f"\nERROR: Gagal menambahkan item. {e}")
    except Exception as e:
        print(f"\nERROR Tidak Terduga: {e}")


# ========================================
# Implementasi Menu Utama
# ========================================

def tampilkan_menu():
    """Menampilkan pilihan menu utama."""
    print("\n\n=== SISTEM MANAJEMEN PERPUSTAKAAN ===")
    print("1. Tambah Item Baru")
    print("2. Tampilkan Semua Item")
    print("3. Cari Item Berdasarkan Judul")
    print("4. Keluar")
    print("-" * 37)


if __name__ == "__main__":
    # Membuat objek Library
    perpustakaan = Library()

    # Data awal (opsional, bisa dihapus jika ingin mulai dari kosong)
    perpustakaan.tambah_item(Book("B001", "Pemrograman Python", "Budi Raharjo"))
    perpustakaan.tambah_item(Magazine("M001", "National Geographic", "Januari 2025"))
    print("\n--- DATA DEMO TELAH DIMASUKKAN ---")
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ").strip()

        if pilihan == '1':
            tambah_item_interaktif(perpustakaan)
        
        elif pilihan == '2':
            perpustakaan.tampilkan_semua_item()
        
        elif pilihan == '3':
            judul_cari = input("Masukkan Judul atau kata kunci: ").strip()
            if judul_cari:
                perpustakaan.cari_item(judul_cari)
            else:
                print("Input judul tidak boleh kosong.")
        
        elif pilihan == '4':
            print("\nTerima kasih telah menggunakan Sistem Perpustakaan Sederhana. Sampai jumpa!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 sampai 4.")