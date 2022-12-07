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

andi = orang('andi','jakarta\n')
andi.perkenalan()

tito = pelajar('tito', 'subang','SMKJP1')
tito.perkenalan()
print(f'saya sekolah di {tito.sekolah}\n')

cahyo = pekerja('cahyo','bandung', 'SMKJP1')
cahyo.perkenalan()
print(f'saya kerja di {cahyo.kantor}')