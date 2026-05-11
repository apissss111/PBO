"""
NON SOLID 3
Masalah: Ketergantungan terlalu kuat
"""

print("=" * 50)
print("NON SOLID 3 - TIGHT COUPLING")
print("=" * 50)


class KeyboardGaming:

    def ketik(self):
        return "Mengetik dengan keyboard gaming"


class Komputer:

    def __init__(self):
        # langsung tergantung ke KeyboardGaming
        self.keyboard = KeyboardGaming()

    def gunakan(self):
        print(self.keyboard.ketik())


pc = Komputer()
pc.gunakan()