"""
SOLID 1
Topik: Single Responsibility Principle (SRP)
Satu class = satu tanggung jawab
"""

print("=" * 50)
print("SOLID 1 - SINGLE RESPONSIBILITY PRINCIPLE")
print("=" * 50)


# =========================
# ANTI PATTERN
# =========================

class PerpustakaanJelek:
    """
    Class ini terlalu banyak tugas:
    - simpan data buku
    - cetak laporan
    - kirim email
    """

    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def tampilkan_buku(self):
        print(f"Buku: {self.judul} - {self.penulis}")

    def cetak_laporan(self):
        print(f"[PDF] Laporan buku {self.judul}")

    def kirim_email(self, email):
        print(f"[EMAIL] Mengirim data buku ke {email}")


print("\n-- Versi Jelek --")
b1 = PerpustakaanJelek("Python Dasar", "Andi")
b1.tampilkan_buku()
b1.cetak_laporan()
b1.kirim_email("admin@gmail.com")


# =========================
# SOLUSI SRP
# =========================

class Buku:
    """Hanya menyimpan data buku"""

    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def tampilkan(self):
        print(f"Buku: {self.judul} - {self.penulis}")


class CetakLaporan:
    """Hanya mencetak laporan"""

    def cetak(self, buku):
        print(f"[PDF] Mencetak laporan {buku.judul}")


class EmailService:
    """Hanya mengirim email"""

    def kirim(self, buku, email):
        print(f"[EMAIL] Mengirim data {buku.judul} ke {email}")


print("\n-- Versi SOLID --")
b2 = Buku("PBO Python", "Budi")
b2.tampilkan()

laporan = CetakLaporan()
laporan.cetak(b2)

email = EmailService()
email.kirim(b2, "user@gmail.com")