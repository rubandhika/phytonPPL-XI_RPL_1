#pewarisan


#Buat 3 objek orang , pelajar , pekerja
#orang = kelas induk
#pelajar , pekerja = kelas turunan


class orang():
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print("halo nama saya", self.nama, "dari", self.asal)

class pelajar(orang):
    def __init__(self, nama, asal, sekolah):
       orang.__init__(self,nama,asal)
       self.sekolah = sekolah

class pekerja(orang): 
    def __init__(self, nama, asal, kantor):
        super(). __init__(nama, asal) #sama dengan orang
        self.kantor = kantor

ruban = orang('ruban','jakarta\n')
ruban.perkenalan()

rafi = pelajar('rafi', 'subang','SMKJP1')
rafi.perkenalan()
print(f'saya sekolah di {rafi.sekolah}\n')

bagus = pekerja('bagus','bandung', 'SMKJP1')
bagus.perkenalan()
print(f'saya kerja di {bagus.kantor}')