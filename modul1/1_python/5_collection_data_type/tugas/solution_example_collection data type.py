# 1) Find max, min
# import math

# list = [23, 57, 76, 6, 60, 28, 30,
# 44, 85, 44, 97, 32, 71, 85,
# 46, 95, 29, 37, 13, 79, 15, 9,
# 23, 10, 22, 78, 46, 2, 99, 3]

# max_num = -math.inf # bisa pake -float('inf')
# min_num = math.inf # bisa pake float('inf')

# for num in list:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num

# print(f'Max number: {max_num}')
# print(f'Min number: {min_num}')

# 2) Count unique ID

# list = [
# 'K0QY6', 'fJU08', 'K0QY6', 'VeZrS', 'jxjQ6', 'sjqom', 'AefAN', 'jxjQ6',
# 'S90wn', 'FZw7F', 'IgYbm', 'dD1ZM', 'sjqom', 'dD1ZM', 'fJU08', 'AefAN',
# 'jxjQ6', 'K0QY6', 'prdDz', 'dD1ZM', 'AefAN', 'WfgpU', 'VeZrS', 'sjqom']

# print(len(set(list)))

# 3) Square Number

# import math
# list = [
#   344, 838, 502, 262, 590, 959, 151, 491, 71, 980, 156, 13, 280, 615, 278, 185,
#   851, 599, 947, 598, 961, 534, 633, 751, 836, 446, 7, 956, 335, 765, 600, 428,
#   595, 478, 667, 628, 375, 402, 663, 728, 704, 182, 377, 380, 49, 253, 566,
#   662, 492, 930, 285, 5, 467, 496, 421, 317, 774, 86, 942, 149, 270, 765, 357,
#   373, 336, 63, 976, 509, 863, 139, 504, 321, 635, 96, 977, 538, 552, 683, 83,
#   752, 576, 350, 538, 79, 164, 414, 579, 948, 971, 121, 354, 562, 562, 63, 385,
#   185, 731, 872, 342, 898]

# squared_list = []

# for num in list:
#     if math.isqrt(num) ** 2 == num:
#         squared_list.append(num)

# print(f'Total square number: {len(squared_list)}')
# print(squared_list)

# 4) film similarity

# film_set = set(input('Your favorite film (comma separated): ').replace("'",'').lower().split(','))
# film_friend_set = set(input('Your friend’s favorite movie (comma separated): ').replace("'",'').lower().split(','))

# print(f'Simmilarity level {round((len(film_set.intersection(film_friend_set)) / len(film_set.union(film_friend_set))) * 100, 2)}%')

# 5) Toko buah List

# listBuah = [
#     ['Apel', 20, 10000],
#     ['Jeruk', 15, 15000],
#     ['Anggur', 25, 20000]
# ]

# cart = []

# while True :
#     pilihanMenu = input('''
#         Selamat Datang di Pasar Buah

#         List Menu :
#         1. Menampilkan Daftar Buah
#         2. Menambah Buah
#         3. Menghapus Buah
#         4. Membeli Buah
#         5. Exit Program

#         Masukkan angka Menu yang ingin dijalankan : ''')

#     if(pilihanMenu == '1') :

#         print('Daftar Buah\n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))

#     elif(pilihanMenu == '2') :

#         namaBuah = input('Masukkan Nama Buah : ')
#         stockBuah = int(input('Masukkan Stock Buah : '))
#         hargaBuah = int(input('Masukkan Harga Buah : '))
#         listBuah.append([namaBuah,stockBuah,hargaBuah])
#         print('Daftar Buah\n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))

#     elif(pilihanMenu == '3') :

#         print('Daftar Buah\n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))
#         indexBuah = int(input('Masukkan index buah yang ingin dihapus : '))
#         del listBuah[indexBuah]
#         print('Daftar Buah\n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))

#     elif(pilihanMenu == '4') :

#         print('Daftar Buah\n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i][0],listBuah[i][1],listBuah[i][2]))
#         while True :
#             indexBuah = int(input('Masukkan index buah yang ingin dibeli : '))
#             qtyBuah = int(input('Masukkan jumlah yang ingin dibeli : '))
#             if(qtyBuah > listBuah[indexBuah][1]) :
#                 print('Stock tidak cukup, stock {} tinggal {}'.format(listBuah[indexBuah][0],listBuah[indexBuah][1]))
#             else :
#                 cart.append([listBuah[indexBuah][0], qtyBuah, listBuah[indexBuah][2], indexBuah])
#             print('Isi Cart :')
#             print('Nama\t| Qty\t| Harga')
#             for item in cart :
#                 print('{}\t| {}\t| {}'.format(item[0], item[1], item[2]))
#             checker = input('Mau beli yang lain? (ya/tidak) = ')
#             if(checker == 'tidak') :
#                 break
#         print('Daftar Belanja :')
#         print('Nama\t| Qty\t| Harga\t| Total Harga')
#         totalHarga = 0
#         for item in cart :
#             print('{}\t| {}\t| {}\t| {}'.format(item[0], item[1], item[2], item[1] * item[2]))
#             totalHarga += item[1] * item[2]    
#         while True :
#             print('Total Yang Harus Dibayar = {}'.format(totalHarga))
#             jmlUang = int(input('Masukkan jumlah uang : '))
#             if(jmlUang > totalHarga) :
#                 kembali = jmlUang - totalHarga
#                 print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
#                 for item in cart :
#                     listBuah[item[3]][1] -= item[1]
#                 cart.clear()
#                 break
#             elif(jmlUang == totalHarga) :
#                 print('Terima kasih')
#                 for item in cart :
#                     listBuah[item[3]][1] -= item[1]
#                 cart.clear()
#                 break
#             else :
#                 kekurangan = totalHarga - jmlUang
#                 print('Uang anda kurang sebesar {}'.format(kekurangan))
                
#     elif(pilihanMenu == '5') :
#         exit()


# 6) Toko buah Dictionary

# # Tipe data yang digunakan pada contoh solusi
# listBuah = [
#     {
#         'nama': 'Apel',
#         'stock': 20,
#         'harga': 10000
#     },
#     {
#         'nama': 'Jeruk',
#         'stock': 15,
#         'harga': 15000
#     },
#     {
#         'nama': 'Anggur',
#         'stock': 25,
#         'harga': 20000
#     }
# ]

# # Contoh tipe data jika menggunakan dictionary dalam dictionary
# listBuahDict = {
#     'ID001':{
#         'nama': 'Apel',
#         'stock': 20,
#         'harga': 10000
#     },
#     'ID002':{
#         'nama': 'Jeruk',
#         'stock': 15,
#         'harga': 15000
#     },
#     'ID003':{
#         'nama': 'Anggur',
#         'stock': 25,
#         'harga': 20000
#     }
# }

# cart = []

# while True :
#     pilihanMenu = input('''
#         Selamat Datang di Pasar Buah

#         List Menu :
#         1. Menampilkan Daftar Buah
#         2. Menambah Buah
#         3. Menghapus Buah
#         4. Membeli Buah
#         5. Exit Program

#         Masukkan angka Menu yang ingin dijalankan : ''')

#     if(pilihanMenu == '1') :

#         print('Daftar Buah\n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) : # for key,val in listBuahDict.items()
#             print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i]['nama'],listBuah[i]['stock'],listBuah[i]['harga'])) # listBuahDict[key][namaKolom]

#     elif(pilihanMenu == '2') :

#         namaBuah = input('Masukkan Nama Buah : ')
#         stockBuah = int(input('Masukkan Stock Buah : '))
#         hargaBuah = int(input('Masukkan Harga Buah : '))
#         listBuah.append({ # kode untuk nambah buah kalo dictionary dalam list
#             'nama': namaBuah,
#             'stock': stockBuah,
#             'harga': hargaBuah
#         }) 
#         print('Daftar Buah\n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i]['nama'],listBuah[i]['stock'],listBuah[i]['harga']))

#     elif(pilihanMenu == '3') :

#         print('Daftar Buah\n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i]['nama'],listBuah[i]['stock'],listBuah[i]['harga']))
#         indexBuah = int(input('Masukkan index buah yang ingin dihapus : '))
#         del listBuah[indexBuah]
#         print('Daftar Buah\n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i]['nama'],listBuah[i]['stock'],listBuah[i]['harga']))

#     elif(pilihanMenu == '4') :

#         print('Daftar Buah\n')
#         print('Index\t| Nama  \t| Stock\t| Harga')
#         for i in range(len(listBuah)) :
#             print('{}\t| {}  \t| {}\t| {}'.format(i,listBuah[i]['nama'],listBuah[i]['stock'],listBuah[i]['harga']))
#         while True :
#             indexBuah = int(input('Masukkan index buah yang ingin dibeli : '))
#             qtyBuah = int(input('Masukkan jumlah yang ingin dibeli : '))
#             if(qtyBuah > listBuah[indexBuah]['stock']) :
#                 print('Stock tidak cukup, stock {} tinggal {}'.format(listBuah[indexBuah]['nama'],listBuah[indexBuah]['stock']))
#             else :
#                 cart.append({
#                     'nama': listBuah[indexBuah]['nama'], 
#                     'qty': qtyBuah, 
#                     'harga': listBuah[indexBuah]['harga'], 
#                     'index': indexBuah
#                 })
#             print('Isi Cart :')
#             print('Nama\t| Qty\t| Harga')
#             for item in cart :
#                 print('{}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga']))
#             checker = input('Mau beli yang lain? (ya/tidak) = ')
#             if(checker == 'tidak') :
#                 break

#         print('Daftar Belanja :')
#         print('Nama\t| Qty\t| Harga\t| Total Harga')
#         totalHarga = 0
#         for item in cart :
#             print('{}\t| {}\t| {}\t| {}'.format(item['nama'], item['qty'], item['harga'], item['qty'] * item['harga']))
#             totalHarga += item['qty'] * item['harga']    
#         while True :
#             print('Total Yang Harus Dibayar = {}'.format(totalHarga))
#             jmlUang = int(input('Masukkan jumlah uang : '))
#             if(jmlUang > totalHarga) :
#                 kembali = jmlUang - totalHarga
#                 print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
#                 for item in cart :
#                     listBuah[item['index']]['stock'] -= item['qty']
#                 cart.clear()
#                 break
#             elif(jmlUang == totalHarga) :
#                 print('Terima kasih')
#                 for item in cart :
#                     listBuah[item['index']]['stock'] -= item['qty']
#                 cart.clear()
#                 break
#             else :
#                 kekurangan = totalHarga - jmlUang
#                 print('Uang anda kurang sebesar {}'.format(kekurangan))
                
#     elif(pilihanMenu == '5') :
#         break
