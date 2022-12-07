# fungsi garis
def garis1():
    print ("===================================")

def garis2():
    print ("-----------------------------------")

#perpus kosong untuk menyimpan buku
buku = []

# fungsi show buku ( perlihatkan buku )
def show_buku():
    if len(buku) <= 0:
        garis1()
        print("buku kosong mas!")
        garis1()
    else:
        for indeks in range(len(buku)):
            garis1()
            print ("[{}] {}".format (indeks, buku [indeks]))
            garis1()

# fungsi untuk edit buku
def edit_buku():
    show_buku()
    indeks = int(input("inputkan ID buku : "))
    if indeks > len(buku):
        print("ID salah")
        garis2()
    else:
        judul_baru = input("judul baru : ")
        buku[indeks] = judul_baru
        garis2()
        print("buku berhasil dirubah!")
        show_buku()
        garis1()

#fungsi insert buku
def insert_buku():
    garis1()
    buku_baru = input("judul buku : ")
    buku.append(buku_baru)
    garis2()
    print("buku berhasil ditambah!")
    garis1()


# fungsi delete buku
def delete_buku():
    show_buku()
    indeks = int(input("inputkan ID buku : "))
    if indeks > len(buku):
        print ("ID salah")
    else:
        buku.remove(buku[indeks])
        garis1()
        print ("buku berhasil dihapus!")
        garis2()



#menu untuk tampilan perpus
def show_Menu():
    print("\n")
    print("-selamat datang di perpus-")
    print("1. show buku")
    print("2. insert buku")
    print("3. edit buku")
    print("4. Delete buku")
    print("5. keluar")

    menu = int(input("pilih menu: > "))

    if menu == 1:
        show_buku()
    elif menu == 2:
        insert_buku()
    elif menu == 3:
        edit_buku()
    elif menu == 4:
        delete_buku()
    elif menu == 5:
        exit()
    else:
        print('upss salah')

# tampikan menu
if __name__ == "__main__":
    while True:
        show_Menu()
    
