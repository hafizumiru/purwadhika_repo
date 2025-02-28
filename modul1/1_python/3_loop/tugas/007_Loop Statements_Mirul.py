import math

# 1  Clear

# spam = input("Input spam: ")
# word = input("Input word: ")

# muncul = 0

# for i in range(0, len(spam)):
#     if spam[i:i+3] == word:
#         muncul += 1

# print("Appeared "+str(muncul)+" times")

# 2 Clear

# spam = input("Input spam: ")

# o = 0
# x = 0

# for i in spam:
#     if i.lower() == "o":
#         o += 1
#     elif i.lower() == "x":
#         x += 1

# if o == x:
#     print(True)
# else:
#     print(False)

# 3 Clear

# numbers = input("Masukan angka yang akan dicheck: ")
# cek_hasil = 0

# for i in numbers:
#     cek_hasil += math.pow(int(i),len(numbers))

# if cek_hasil == int(numbers):
#     print(numbers + " is narcisstic number")
# else:
#     print(numbers + " is not narcisstic number")

# 4

# name = input("Masukan Nama Lengkap anda: ")
# nama_depan = name[0].upper()
# nama_belakang = "nama"

# for i in range(len(name)-1,-1,-1):
#     if name[i] == " ":
#         nama_belakang = name[i+1].upper()
#         break

# print("Inisial nama anda adalah " + nama_depan +"."+nama_belakang)

# 5

# n = int(input("Masukan angka Faktorial: "))
# hasil = 1

# for i in range(n, 1, -1):
#     hasil *= i
# print(hasil)
