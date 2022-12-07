# public 1
class siswa:
    def __init__(self, siswa):
        self.siswa = siswa

tampilan = siswa("ruban")

print(f'siswa kami bernama {tampilan.siswa} ganteng')


# protected class 2
class guru:
    def __init__(self, nama):
        self._nama = nama

class anita(guru):
    def __init__(self, nama):
        super().__init__(nama)

    def menampilkan(self):
        print(f'guru kami bernama {self._nama} yang cantik')

buguru = anita('bu anita')
buguru.menampilkan()


#private class 3
class kepsek:
    def __init__(self, nama):
        self.__nama = nama

    def tampilkan_nama(self):
        print(f'kepsek kami bernama {pak.__nama}')

pak = kepsek('pak lilik')
pak.tampilkan_nama()