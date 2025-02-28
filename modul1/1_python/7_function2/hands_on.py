def tambah(angka1, angka2):
    return angka1 + angka2

def kurang(angka1, angka2):
    return angka1 - angka2

def kali(angka1, angka2):
    return angka1 * angka2

def bagi(angka1, angka2):
    return angka1 / angka2

def pangkat(angka1, angka2):
    return angka1 ** angka2

def bagiBulat(angka1, angka2):
    return angka1 // angka2

def bagiSisa(angka1, angka2):
    return angka1 % angka2

# for i in range(5):
#     print(i)

# print(i)
# print(tambah(5,7))
# angka3 = 12
# print(total + angka3)
x = 5
def coba():
    # x = 2
    global x
    x += 8
    print(x + 2)
    return x + 3


# y = coba()
# print(y)
# print(coba(), x)

def hitung(namaFungsi, angka1, angka2):
    return namaFungsi(angka1, angka2)

# print(hitung(bagiSisa, 1000, 3))
# print(hitung(bagiBulat, 1000, 3))

def tampilkanHasil(namaFungsi, angka1, angka2):
    if namaFungsi.lower == 'tambah':
        print('Hasil penjumlahan adalah: ', tambah(angka1, angka2))
    elif namaFungsi.lower == 'kurang':
        print('Hasil pengurangan adalah: ', kurang(angka1, angka2))
    elif namaFungsi.lower == 'kali':
        print('Hasil perkalian adalah: ', kali(angka1, angka2))
    elif namaFungsi.lower == 'bagi':
        print('Hasil pembagian adalah: ', bagi(angka1, angka2))
    else:
        print('Hasilnya adalah: ', bagiBulat(angka1, angka2), bagiSisa(angka1, angka2))

# namaFungsi = input('nama fungsi: ')
# angka1 = int(input('angka pertama: '))
# angka2 = int(input('angka kedua: '))

# tampilkanHasil(namaFungsi, angka1, angka2)

# def countdown(counter):
#     print(counter)
#     counter -= 1
    
#     if(counter >= 0):
#         # counter -= 1
#         countdown(counter)
#     # counter -= 1
# countdown(3)



# ganjil_or_genap = 'Ganjil' if angka1 % 2  == 1 else 'Genap'

my_list = [2, 3, 4, 5]
new_list = [item ** 3 for item in my_list]

list1 = [1, 2, 3, 4, 5]
list2 = [2 * a for a in list1 if a % 2 == 1]
# print(list2)

kurang = lambda angka1, angka2, angka3 : angka1 - angka2 - angka3
# print(kurang(20,4,6))

kali2 = lambda angka : angka * 2

hasilMapList1 = list(map(kali2, list1))
# print(hasilMapList1)

def mapDuplikat(namaFunction, collection): # cara kerja map function
    return [namaFunction(item) for item in collection]
    
def ubah(angka):
    return 'Angka {}'.format(angka)

print(mapDuplikat(ubah, list1))

print(mapDuplikat(lambda angka: 'Angka {}'.format(angka), list1))

def angkaGenap(angka):
    return angka % 2 == 0

hasilFilterList1 = list(filter(angkaGenap, list1))

hasilFilterList1 = list(filter(lambda angka : angka % 2 == 0, list1))
print(hasilFilterList1)