# jenis enkapsulasi : public, proctected, private


# membuat public class 
class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

# instansiasi 
segitiga_besar = segitiga(100, 80)

#print
print('ini adalah public class')
print(f'alas : {segitiga_besar.alas}')
print(f'tinggi : {segitiga_besar.tinggi}')
print(f'luas : {segitiga_besar.luas}\n')




# membuat protected class
class mobil: #class induk 
    def __init__(self, merk):
        self._merk = merk #protected class declaration

# instansiasi (turunan)
class mobilefwan(mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk) #panggil merk dibagian sini 
        self._total_gear = total_gear

    def pamer(self):
        # hak akses _merk dari subclass
        print (f'ini adalah mobil {self._merk} dengan total gear nya {self._total_gear}\n')

#instansiasi 
print('ini adalah protected class')
ferrari = mobilefwan('ferrari', 8)
ferrari.pamer()



# membuat private class
class motor:
    def __init__(self, merk):
        self.__merk  = merk #private class declaration

    def tampilkan_merk(self):
        print(f'merk motornya : {moge.__merk}')
    #panggil private disini 

# instansiasi 
print('ini adalah private class')
moge = motor('harley')
moge.tampilkan_merk()