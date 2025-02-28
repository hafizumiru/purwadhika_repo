umurPemohonSIM = [17, 2, 39, 55, 90, 150, -20, 46, 7, 18]

# i = 0 # base statement

# while i < len(umurPemohonSIM): # loop condition
#     if umurPemohonSIM[i] >= 17 and umurPemohonSIM[i] <= 100:
#         print("Umur " + str(umurPemohonSIM[i]) + " Lulus")
#     elif umurPemohonSIM[i] < 17 and umurPemohonSIM[i] >= 0:
#         print("Umur " + str(umurPemohonSIM[i]) + " Tidak lulus")
#     elif umurPemohonSIM[i] < 0:
#         print('Umur tidak valid')
#     else:
#         print("Bau tanah")
#     i += 1 # compound statement

# for umur in umurPemohonSIM:
#     if umur >= 17 and umur <= 100:
#         print("Umur " + str(umur) + " Lulus")
#     elif umur < 17 and umur >= 0:
#         print("Umur " + str(umur) + " Tidak lulus")
#     elif umur < 0:
#         print('Umur tidak valid')
#     else:
#         print("Bau tanah")


sentence = '#2019gantipresiden!'
# print(sentence)
# i = 0
# while i < len(sentence):
#     if sentence[i] == '#':
#         print(True)
#     print(sentence[i])
#     i += 1

# for huruf in sentence:
#     if huruf == '#':
#         print(True)
#         break
#     print(huruf)

# for i in range(len(sentence)):
#     if sentence[i] == '#':
#         print(True)

dataPemohonSIM = []

# while True:
#     try:
#         dataPemohonInput = input("Masukkan umur anda (ketik 'selesai' jika sudah selesai): ")
#         if dataPemohonInput == 'selesai':
#             break
#         else:
#             dataPemohonSIM.append(int(dataPemohonInput))
            
#     except:
#         print('Input berupa non angka, silakan coba lagi')
    
# print("List umur pemohon SIM: ", dataPemohonSIM)

# i = 1
# while i <= 10:
#     print(i)
#     i += 3

# for i in range(1, 11, 3):
#     print(i)

# i = 10
# while i >= 0:
#     print(i)
#     i -= 3

# for i in range(10, 0, -3):
#     print(i)

quote = 'nasionalis agamis komunis mas anis istigfar'

substring = 'is'

# for i in range(0, len(quote), 1):
#     if(quote[i:i+len(substring)] == substring):
#         print(True)
#         break

# print(quote[8:10]) # nasionalis
# print(quote[15:17]) # agamis
# print(quote[23:25]) # komunis
# print(quote[32:34]) # mas anis
# print(quote[34:36]) # istigfar

# for karakter in quote:
#     print(karakter)

# for i in range(0, len(quote), len(substring)):
#     for j in range(0,len(substring)):
#         print(i+j)
# for i in range(0, len(quote), 1):
#     if(quote[i:i+len(substring)] == substring):
#         print(quote[i:i+len(substring)])
# print(len(str(5)))

# for i in range(10000):
#     if len(str(i)) == 1:
#         if (i == 3):
#             continue
#         else:
#             print(i)
#     else:
#         flag = True
#         i = str(i)
#         for number in i:
#             # print(type(number))
#             if(number == '3'):
#                 flag = False
#                 break
#         if flag:
#             print(i)
#         else:
#             continue

stars = ''
size = 5
for i in range(size):
    for j in range(i, size):
        stars += '* '
    stars += '\n'

print(stars)
