# fungsi garis
def garis():
    print("=========================")

# selamat datang di jp hotel
garis()
print("selamat datang , di jp hotel--")
print("--no------tipe----------harga--")
print("--01------suite--------1.000.000--")
print("--02------royal---------500.000--")
print("--03------bpjs----------250.000--")

# sampe resepsionis (input data)
garis()
cust = input("masukan mana lengkap :")
tipe = int(input("tipe kamar :"))
lama_inap = int(input("masukkan nama inap :"))

# tipe kamar
garis()
if tipe == 1:
    tipe_kamar = ("suite")
elif tipe == 2:
    tipe_kamar = ("royal")
elif tipe == 3:
    tipe_kamar = ("BPJS")

#kalkulasi harga total
if tipe == 1:
    total_harga = 1000000 * lama_inap
elif tipe == 2:
    total_harga = 500000 * lama_inap
elif tipe == 3:
    total_harga = 250000 * lama_inap

# struk jphotel
garis()
print("pelanggan atas nama : ", cust )
print("tipe kamar yang dipilih : " , tipe_kamar)
print("lama menginap : " , lama_inap)
garis()
print("TOTAL : ","Rp", total_harga , ",00")
