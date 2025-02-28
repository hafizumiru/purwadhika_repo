# 1) Bilangan prima

number = int(input("number = "))

for i in range(2, int(number ** 0.5) + 1):
    if number == 2:
        pass
    elif (number % i == 0):
        print(f"{number} bukan merupakan bilangan prima")
        break
else:
    print(f"{number} merupakan bilangan prima")

# alternatif solusi/algoritma

number = int(input("masukkan input angka = "))
count = 0
for i in range(1,number+1):
    if number == 2:
        print("bilangan prima")
        break
    if number % i == 0:
        count += 1
    elif number % i == 1:
        count += 0

if count == 2:
    print("bilangan prima")

if count > 2:
    print("bukan bilangan prima")

# 2) Cek alphanum, alphabet, digit, lower sama upper

characters = "qA2"

boolAlnum = False
for char in characters.split():
    if(char.isalnum):
        boolAlnum = True
        break
    
boolAlpha = False
for char in characters.split():
    if(char.isalpha):
        boolAlpha = True
        break

boolDigit = False
for char in characters.split():
    if(char.isdigit):
        boolDigit = True
        break
    
boolUpper = False
for char in characters.split():
    if(char.isupper):
        boolUpper = True
        break
    
boolLower = False
for char in characters.split():
    if(char.islower):
        boolLower = True
        break
    
print(boolAlnum)
print(boolAlpha)
print(boolDigit)
print(boolUpper)
print(boolLower)

# 3) Bentuk gambar (Loop Drawing)

# bentuk 1

stars = ''
size = 5

for i in range(size) :
    for j in range(size - i) :
        stars += '* '
    stars += '\n'

for i in range(1, size) :
    for j in range(i + 1) :
        stars += '* '
    stars += '\n'

print(stars)

# * * * * * 
# * * * *
# * * *
# * *
# *
# * *
# * * *
# * * * *
# * * * * *

# bentuk 2

stars = ''
size = 5

for i in range(size) :
    for j in range(size - i) :
        stars += '  '
    for k in range(i * 2 + 1) :
        stars += '* '
    stars += '\n'

for i in range(1, size) :
    for j in range(i + 1) :
        stars += '  '
    for k in range((size * 2) - (i * 2) - 1) :
        stars += '* '
    stars += '\n'

print(stars)

#           *
#         * * *
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *

# 4) Palindrom

# Algoritma 1: loop

string_input = input('Masukkan string: ')
string_terbalik = ''

for i in range(len(string_input) - 1, -1, -1):
    string_terbalik += string_input[i]

if(string_input_lower == string_input.lower()):
    print(string_input, 'is a palindrome')
else:
    print(string_input, 'is not a palindrome')

# Algoritma 2: slicing

# string_kebalik = string_input[::-1]

# if(string_input == string_kebalik):
#     print(string_input, 'is a palindrome')
# else:
#     print(string_input, 'is not a palindrome')

# 5) Pangram

alphabet = "abcdefghijklmnopqrstuvwxyz"
pangram_status = True
for char in alphabet:
    if char not in string_input.lower():
        pangram_status = False

if(pangram_status):
    print('Kalimat tersebut adalah pangram')
else:
    print('Kalimat tersebut bukan pangram')

# 6) Toko buah

hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

stockApel = 5
stockJeruk = 7
stockAnggur = 6

while(True) :
    jumlahApel = int(input('Masukkan Jumlah Apel : '))
    if(jumlahApel > stockApel) :
        print('Jumlah yang dimasukkan terlalu banyak \nStock Apel tinggal : ' + str(stockApel))
    else :
        break
while(True) :
    jumlahJeruk = int(input('Masukkan Jumlah Jeruk : '))
    if(jumlahJeruk > stockJeruk) :
        print('Jumlah yang dimasukkan terlalu banyak \nStock Jeruk tinggal : ' + str(stockJeruk))
    else :
        break
while(True) :
    jumlahAnggur = int(input('Masukkan Jumlah Anggur : '))
    if(jumlahAnggur > stockAnggur) :
        print('Jumlah yang dimasukkan terlalu banyak \nStock Anggur tinggal : ' + str(stockAnggur))
    else :
        break

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

while(True) :
    jmlUang = int(input('Masukkan jumlah uang : '))

    if(jmlUang > totalHarga) :
        kembali = jmlUang - totalHarga
        print('Terima kasih \n\nUang kembali anda : {}'.format(kembali))
        break
    elif(jmlUang == totalHarga) :
        print('Terima kasih')
        break
    else :
        kekurangan = totalHarga - jmlUang
        print('Uang anda kurang sebesar {}'.format(kekurangan))
