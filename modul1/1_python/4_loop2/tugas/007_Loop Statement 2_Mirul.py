# # 1

# number = int(input("Masuk kan angka: "))

# for i in range(3, number+1):
#     if number%(i-1) == 0:
#         print(str(number)+" bukan merupakan bilangan prima")
#         break
#     if i == number:
#         print(str(number)+" merupakan bilangan prima")


# # 2

# S = input("Masukan String: ")

# for char in S:
#     if char.isalnum():
#         print(True)
#         break
# for char in S:
#     if char.isalpha():
#         print(True)
#         break
# for char in S:
#     if char.isdigit():
#         print(True)
#         break
# for char in S:
#     if char.islower():
#         print(True)
#         break
# for char in S:
#     if char.isupper():
#         print(True)
#         break

# 3

# stars = ""
# size = 5

# for i in range(size):
#     stars += "\n"
#     for j in range(size-i):
#         stars += "* "

# for i in range(size-1):
#     stars += "\n"
#     for j in range(i+2):
#         stars += "* "

# print(stars)

# diamond = ""
# size = 9

# atas
# for i in range(size // 2 + 1):
#     for j in range(size // 2 - i):
#         diamond += "  "
#     for j in range(i * 2 + 1):
#         diamond += "* "
#     diamond += "\n"

# # bawah
# for i in range(size // 2 - 1, -1, -1):
#     for j in range(size // 2 - i):
#         diamond += "  "
#     for j in range(i * 2 + 1):
#         diamond += "* "
#     diamond += "\n"

# print(diamond)

# 4

# input = input("Masukan kata atau kalimat: ")
# balik = ''

# for i in range(len(input) - 1, -1, -1):
#     balik += input[i]

# if input.lower()== balik.lower():
#     print(input + ' adalah sebuah palindrom!')
# else:
#     print(input + ' adalah bukan palindrom!')

# 5

# kalimat = input("Masukan kalimat: ")
# abjad = 'abcdefghijklmnopqrstuvwxyz'

# for char in abjad:
#     if char in kalimat:
#         continue
#     else:
#         print('Kalimat tersebut bukan sebuah pangram')
#         break
# else:
#     print('Kalimat tersebut adalah sebuah pangram!')

# 6

# stok_apel = 10
# stok_jeruk = 10
# stok_anggur = 10

# apel = int(input("Masukan Jumlah Apel: "))
# while apel > stok_apel:
#     print("Jumlah yang dimasukkan terlalu banyak, stok apel tinggal", stok_apel)
#     apel = int(input("Masukan Jumlah Apel: "))

# jeruk = int(input("Masukan Jumlah Jeruk: "))
# while jeruk > stok_jeruk:
#     print("Jumlah yang dimasukkan terlalu banyak, stok jeruk tinggal", stok_jeruk)
#     jeruk = int(input("Masukan Jumlah Jeruk: "))

# anggur = int(input("Masukan Jumlah Anggur: "))
# while anggur > stok_anggur:
#     print("Jumlah yang dimasukkan terlalu banyak, stok anggur tinggal", stok_anggur)
#     anggur = int(input("Masukan Jumlah Anggur: "))

# total_apel = apel * 10000
# total_jeruk = jeruk * 15000
# total_anggur = anggur * 20000

# total_belanja = total_apel + total_jeruk + total_anggur

# print("Detail Belanja")
# print("Apel : "+str(apel)+" x 10000 = " + str(total_apel))
# print("Apel : "+str(jeruk)+" x 10000 = " + str(total_jeruk))
# print("Apel : "+str(anggur)+" x 10000 = " + str(total_anggur))
# print("Total : " + str(total_belanja))

# bayar = int(input("Masukan jumlah uang : "))
# while bayar < total_belanja:
#     print("Uang anda kurang sebesar " + str(total_belanja - bayar))
#     bayar = int(input("Masukan jumlah uang : "))
# if bayar == total_belanja:
#     print("Terimakasih")
# elif bayar > total_belanja:
#     print("Terimakasih\nUang kembali anda : " + str(bayar - total_belanja))
