class PersegiPanjang():
    def __init__(self, p, l):
        # fungsi dipanggul pertama kali saat object diciptakan
        self.p = p
        self.l = l

    def info(self):
        return f'Menghitung persegi panjang dengan panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l