# 4 objek
#  kubus, tabung, bola, balok

#fungsi garis
def garis():
    print("---------------------------------")

# SELAMAT DATANG DI Java Tengah
garis()
print("--Selamat Datang DI Java Tengah--")
garis()

class bangun_ruang:
    print("-- kubus--")
    print("-- tabung--")
    print("-- bola--")
    print("-- balok--")
garis()

#input data
tipe = int(input("Masukkan bangunan yg ingin dijumlah : "))


class kubus:
    def __init__(self, sisi):
        self._sisi = sisi

    def tampilkan_kubus(self, sisi):
        self.sisi = sisi

        print("sisi = ", sisi)

class tabung:
    def __init__(self, r ,tinggi):
        self._r = r
        self._tinggi = tinggi

    def tampilkan_tabung(self, r, tinggi):
        self.r = r
        self.tinggi = tinggi

        print("r = ", r)
        print("tinggi = ", tinggi)


class bola:
    def __init__(self, luas, ruang):
        self._luas = luas
        self._ruang = ruang

    def tampilkan_bola(self, luas, ruang):
        self.luas = luas
        self.ruang = ruang

        print("luas = ", luas)
        print("ruang = ", ruang)


class balok:
    def __init__(self, panjang, lebar, tinggi):
        self._panjang = panjang
        self._lebar = lebar
        self._tinggi = tinggi

    def tampilkan_balok(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

        print("panjang = ", panjang)
        print("lebar = ", lebar)
        print("tinggi = ", tinggi)


# tipe luas
if tipe == 1:
    Luas_bangun = ("kubus")

    sisi = int(input("Masukkan sisi : "))

    print("sisi = ", sisi)
    print("Hasilnya = ",sisi * sisi * sisi)

    garis()

elif tipe == 2:
    Luas_bangun = ("tabung")

    r = int(input("Masukkan r : "))
    tinggi = int(input("Masukkan tinggi : "))

    print("r = ", r)
    print("tinggi", tinggi)
    print("Hasilnya = ", 22 * r* r /7 * tinggi)
    
    garis()

elif tipe == 3:
    Luas_bangun = ("bola")

    luas = int(input("masukkan luas : "))
    r = int(input("masukkan ruang : "))
    
    print("r = ", r)
    print("Hasilnya = ", 4 * 22 * r *r /7)
    garis()


elif tipe == 4:
    Luas_bangun = ("balok")
    
    panjang = int(input("Masukkan panjang : "))
    lebar = int(input("Masukkan lebar : "))
    tinggi = int(input("masukkan tinggi : "))

    print("panjang = ", panjang)
    print("lebar = ", lebar)
    print("tinggi = ", tinggi)
    print("Hasilnya = ", panjang * lebar * tinggi)
