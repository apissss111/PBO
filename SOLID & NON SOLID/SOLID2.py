"""
SOLID 2
Topik: Open Closed Principle (OCP)
Class terbuka untuk pengembangan,
tetapi tertutup untuk modifikasi.
"""

print("=" * 50)
print("SOLID 2 - OPEN CLOSED PRINCIPLE")
print("=" * 50)


# =========================
# ANTI PATTERN
# =========================

class DiskonJelek:

    def hitung_diskon(self, tipe, harga):

        if tipe == "pelajar":
            return harga * 0.1

        elif tipe == "member":
            return harga * 0.2

        elif tipe == "vip":
            return harga * 0.3


print("\n-- Versi Jelek --")
dj = DiskonJelek()

print("Pelajar :", dj.hitung_diskon("pelajar", 100000))
print("Member  :", dj.hitung_diskon("member", 100000))


# =========================
# SOLUSI OCP
# =========================

class Diskon:
    def hitung(self, harga):
        pass


class DiskonPelajar(Diskon):

    def hitung(self, harga):
        return harga * 0.1


class DiskonMember(Diskon):

    def hitung(self, harga):
        return harga * 0.2


class DiskonVIP(Diskon):

    def hitung(self, harga):
        return harga * 0.3


class Kasir:

    def __init__(self, diskon):
        self.diskon = diskon

    def total_diskon(self, harga):
        return self.diskon.hitung(harga)


print("\n-- Versi SOLID --")

pelajar = Kasir(DiskonPelajar())
member = Kasir(DiskonMember())
vip = Kasir(DiskonVIP())

print("Pelajar :", pelajar.total_diskon(100000))
print("Member  :", member.total_diskon(100000))
print("VIP     :", vip.total_diskon(100000))