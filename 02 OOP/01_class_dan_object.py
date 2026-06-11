class Kampus():
    nama = ''
    alamat = ''

class Mahasiswa():
    nama = ''
    nim = 0
    def perkenalan(self):
        print(f'Perkenalkan nama saya {self.nama} dengan NIM {self.nim}')

kampus1 = Kampus()
kampus1.nama = 'Universitas Indonesia'
kampus1.alamat = 'Depok'

mahasiswa1 = Mahasiswa()
mahasiswa1.nama = 'Budi'
mahasiswa1.nim = 123456789
mahasiswa1.perkenalan()

