#latihan overloading

class angka:
    def __init__(self, angka):
        self.angka = angka

    def __add__(self, objek): #magic method
        return self.angka * objek.angka

x1 = angka(20)
x2 = angka(30)
print (x1 + x2) 