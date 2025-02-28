# 8
# Bilangan ganjil/genap
angkaUser = int(input("Please input your number: "))

if angkaUser % 2 == 0:
    print("Number {} is even".format(angkaUser))
else:
    print("Number {} is odd".format(angkaUser))

# 9
# Hitung IMT/BMI
import math
print('')
massa = int(input('Masukkan Massa (kg) : '))
tinggi = int(input('Masukkan Tinggi (m) : ')) / 100
print('')
IMT = massa / (tinggi**2) 

if IMT < 18.5 :
    print(f"(1) Indeks {IMT}. Berat Badan Kurang!")
elif 18.5 <= IMT <= 24.9:
    print(f"(1) Indeks {IMT}. Berat Badan Ideal!")
elif 25.0 <= IMT <= 29.9:
    print(f"(1) Indeks {IMT}. Berat Badan Berlebih!")
elif 30.0 <= IMT <= 39.9:
    print(f"(1) Indeks {IMT}. Berat Badan Sangat Berlebih!")
else:
    print(f"(1) Indeks {IMT}. Obesitas!")

print('')

# 10
# Toko buah lanjutan
hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

jumlahApel = int(input('Masukkan Jumlah Apel : '))
jumlahJeruk = int(input('Masukkan Jumlah Jeruk : '))
jumlahAnggur = int(input('Masukkan Jumlah Anggur : '))

totalHargaApel = jumlahApel * hargaApel
totalHargaJeruk = jumlahJeruk * hargaJeruk
totalHargaAnggur = jumlahAnggur * hargaAnggur
totalHarga = totalHargaAnggur+totalHargaApel+totalHargaJeruk

print('''
Detail Belanja

Apel : {jmlApel} x {hrgApel} = {totalHrgApel}
Jeruk : {jmlJeruk} x {hrgJeruk} = {totalHrgJeruk}
Anggur : {jmlAnggur} x {hrgAnggur} = {totalHrgAnggur}

Total : {totalHarga}
'''.format(jmlApel=jumlahApel, hrgApel=hargaApel, totalHrgApel=totalHargaApel, 
    jmlJeruk=jumlahJeruk, hrgJeruk=hargaJeruk, totalHrgJeruk=totalHargaJeruk,
    jmlAnggur=jumlahAnggur, hrgAnggur=hargaAnggur, totalHrgAnggur=totalHargaAnggur,
    totalHarga=totalHarga))

jmlUang = int(input('Masukkan jumlah uang : '))

if(jmlUang > totalHarga) :
    kembali = jmlUang - totalHarga
    print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
elif(jmlUang == totalHarga) :
    print('Terima kasih')
else :
    kekurangan = totalHarga - jmlUang
    print('Transaksi anda dibatalkan \nuangnya kurang sebesar {}'.format(kekurangan))

# 11
# Bilangan weird dan not weird

checkNumber = int(input("Input your number: "))

if(checkNumber % 2 == 1):
    print("Weird")
else:
    if(2 <= checkNumber <= 5):
        print("Not Weird")
    elif(6 <= checkNumber <= 20):
        print("Weird")
    elif(checkNumber > 20):
        print("Not Weird")
    else:
        print("Not a Valid Number") # Jika angkanya 0 atau minus

# 12
# Masukin nama
first_name = input("Masukkan nama depan Anda: ")
last_name = input("Masukkan nama belakang Anda: ")

print("Hello " + first_name + " " + last_name + "! You just delved into python.")

# 13
# Dari ( ) spasi jadi - (dash/strip)
kalimatUbah = input("Masukkan kalimat yang ingin diubah: ")
print(kalimatUbah.replace(" ", "-"))

# 14
# Divmod manual

inputA = int(input("Angka pertama: "))
inputB = int(input("Angka kedua: "))

divAB = inputA // inputB
modAB = inputA % inputB

print(divAB)
print(modAB)
print("(" + str(divAB) + "," + str(modAB) + ")")