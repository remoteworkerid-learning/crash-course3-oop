from geometri.bangun_ruang import BangunRuang
from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import SegiTiga

print('Menggunakan OOP')
print('\nLuas Persegi Panjang')
p1 = PersegiPanjang(10, 3)
print (p1.info())
print(f'Luasnya adalah {p1.hitung_luas()}')
print('\nLuas Segi Tiga')
p2 = SegiTiga(10, 6)
print(p2.info())
print(f'Luasnya adalah {p2.hitung_luas()}')

print('\nMencoba membuat object dari kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())
