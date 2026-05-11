"""
NON SOLID 1
Masalah: Satu class melakukan semuanya
"""

print("=" * 50)
print("NON SOLID 1 - GOD CLASS")
print("=" * 50)


class SistemSekolah:

    def tambah_siswa(self):
        print("Tambah siswa")

    def cetak_rapor(self):
        print("Cetak rapor")

    def kirim_email(self):
        print("Kirim email")

    def koneksi_database(self):
        print("Connect database")

    def hitung_gaji_guru(self):
        print("Hitung gaji guru")


s = SistemSekolah()

s.tambah_siswa()
s.cetak_rapor()
s.kirim_email()
s.koneksi_database()
s.hitung_gaji_guru()