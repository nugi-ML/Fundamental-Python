class Mahasiswa:
    nim = 0
    nama = ""

    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
    
    def __str__(self):
        return f"Mahasiswa : {self.nim} - {self.nama}"

    def __eq__(self, other):
        return self.nim == other.nim and self.nama == other.nama
    
mhs1 = Mahasiswa(123, "Budi")
print(mhs1.nim)
print(mhs1.nama)
print(mhs1)

mhs2 = Mahasiswa(123, "Nugi")
print(mhs2)
print(mhs1 == mhs2)