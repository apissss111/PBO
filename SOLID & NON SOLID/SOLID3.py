"""
SOLID 3
Topik: Dependency Inversion Principle (DIP)
Class tingkat tinggi tidak boleh
bergantung langsung pada class rendah.
"""

print("=" * 50)
print("SOLID 3 - DEPENDENCY INVERSION PRINCIPLE")
print("=" * 50)


# =========================
# ANTI PATTERN
# =========================

class MySQLDatabase:

    def connect(self):
        return "Terhubung ke MySQL"


class AplikasiJelek:

    def __init__(self):
        self.database = MySQLDatabase()

    def jalankan(self):
        print(self.database.connect())


print("\n-- Versi Jelek --")
app = AplikasiJelek()
app.jalankan()


# =========================
# SOLUSI DIP
# =========================

class Database:

    def connect(self):
        pass


class MySQL(Database):

    def connect(self):
        return "Terhubung ke MySQL"


class MongoDB(Database):

    def connect(self):
        return "Terhubung ke MongoDB"


class Aplikasi:

    def __init__(self, database):
        self.database = database

    def jalankan(self):
        print(self.database.connect())


print("\n-- Versi SOLID --")

mysql = Aplikasi(MySQL())
mysql.jalankan()

mongo = Aplikasi(MongoDB())
mongo.jalankan()