"""
NON SOLID 2
Masalah: Terlalu banyak if else
"""

print("=" * 50)
print("NON SOLID 2 - IF ELSE BERLEBIHAN")
print("=" * 50)


class Pembayaran:

    def bayar(self, metode):

        if metode == "cash":
            print("Bayar pakai cash")

        elif metode == "qris":
            print("Bayar pakai QRIS")

        elif metode == "transfer":
            print("Bayar pakai transfer")

        elif metode == "ewallet":
            print("Bayar pakai e-wallet")

        elif metode == "credit":
            print("Bayar pakai kartu kredit")


p = Pembayaran()

p.bayar("cash")
p.bayar("qris")
p.bayar("transfer")