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

# for i in range(len(sentence)):
#     if sentence[i] == '#':
#         print(True)

dataPemohonSIM = []

while True:
    try:
        dataPemohonInput = input("Masukkan umur anda (ketik 'selesai' jika sudah selesai): ")
        if dataPemohonInput == 'selesai':
            break
        else:
            dataPemohonSIM.append(int(dataPemohonInput))
            
    except:
        print('Input berupa non angka, silakan coba lagi')
    
print("List umur pemohon SIM: ", dataPemohonSIM)

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