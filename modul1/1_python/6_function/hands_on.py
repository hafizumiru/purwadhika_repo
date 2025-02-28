def samlekum():
    print('Assalamualaikum Wrwb')
    print('Shalom')
    print('Om swastiastu')
    print('Salam kebajikan')
    print('Salam Einstein')
    # return 5
# samlekum()
# print(samlekum())

def kumsalam(nama,kelamin=''):
    if kelamin.lower() == 'pria' or kelamin.lower() == 'cowo' or kelamin.lower() == 'laki-laki':
        print(f'Walaikumsalam, mas {nama}.')
    elif kelamin.lower() == 'wanita' or kelamin.lower() == 'cewe' or kelamin.lower() == 'perempuan':
        print(f'Walaikumsalam, mbak {nama}.')
    elif kelamin.lower() == 'cwk':
        print(f'Sabar ya Azril, aku lagi cari posisi yang pas buat cukur bulu-bulu you')
    else:
        print(f'Alien')


# kumsalam('Andi','PRIA')
# kumsalam('Andre','cwk')
# kumsalam('Mark Zukebes')
# namaUser = input('Masukan nama anda: ')
# kelaminUser = input('Cek selangkangan: ')
# kumsalam(namaUser, kelaminUser)

# inputUmur = input()
# if(inputUmur.isdigit()):
#     inputUmur = int(inputUmur)
# else:
#     print('Input bukan angka')

def tambah(angka1, angka2):
    return angka1 + angka2
tambah(2,2)
# print(print('print'))
angka = tambah(2,2)
# print(angka)

# def tambah_print(angka1, angka2):
#     hasil = angka1 + angka2
#     print(f'Hasilnya adalah: {hasil}')
#     return hasil
# print(tambah_print(9,9))

# angka1 = int(input('masukan angka 1: '))
# angka2 = int(input('masukan angka 2: '))
# print(f'Hasil penjumlahan {angka1} dan {angka2} adalah {tambah(angka1,angka2)}')

listContoh = ['hello', 1, 1, 3, True]

def print_list(listContoh, slice1 = -1, slice2 = -1):
    if(slice1 < 0 and slice2 >= 0):
        print(listContoh[:slice2])
    elif(slice2 < 0 and slice1 >= 0):
        print(listContoh[slice1:])
    elif(slice1 >= 0 and slice2 >= 0):
        print(listContoh[slice1:slice2])
    else:
        print(listContoh[:])
print_list(listContoh, slice2 = 4, slice1 = 1)