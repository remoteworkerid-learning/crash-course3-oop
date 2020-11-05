from geometri.bangun_ruang import BangunRuang


class SegiTiga(BangunRuang):
    def __init__(self, a, t):
        self.a = a
        self.t = t

    def info(self):
        return f'Menghitung luas segitiga dengan alas = {self.a} dan tinggi = {self.t}'
    def hitung_luas(self):
        return self.a * self.t / 2