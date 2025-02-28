# 1) Mencari kata dalam string

spam = 'ababaababbbbcccbabcc'
word = 'bab'

a = len(spam)
b = len(word)
count = 0

for i in range(a-b+1):
    if spam[i:i+b] == word:
        count +=1

print(f"appeared {count} times")

# 2) Jumlah o dan x (peka huruf besar-kecil/case sensitive)

spam = "ooxx"

panjang_o, panjang_O = 0, 0
panjang_x, panjang_X = 0, 0

for i in spam:
    if i == "o":
        panjang_o += 1
    elif i == "x":
        panjang_x += 1
    elif i == "O":
        panjang_O += 1
    elif i == "X":
        panjang_X += 1
    else:
    	"Error, bukan itu yang diminta"

print(panjang_x == panjang_o and panjang_X == panjang_O)

# 3) Bilangan narsistik

spam=input("Masukkan angka: ")
digitTotal=len(spam)
count=0

for i in range(digitTotal):
    count=count+pow(int(spam[i]),digitTotal)

if count==int(spam):
    print(spam, "is a narcissistic number")
else:
    print(spam, "not a narcissistic number")

# contoh solusi alternatif

angka = int(input("Masukkan sebuah angka: "))
angkaStr = str(angka)
n = len(angkaStr)
totalPangkat = sum(int(digit) ** n for digit in angkaStr) # Generator Expression

if totalPangkat == angka:
    print(f"(4) {angka} adalah bilangan narsistik.")
else:
    print(f"(4) {angka} bukan bilangan narsistik.")

# 4) Inisial Nama depan & belakang

name = "Median Hardiv Nugraha"

result = ""
for i in range(len(name)):
    if i == 0:
        result += name[i]
    if name[i] == " ":
        result += name[i + 1]

print(result[0].title() + "." + result[-1].title())

# alternatif tanpa for loop

nama = input("Masukkan nama: ")

splitnama = nama.split(" ")

print(splitnama[0][0].title(),".",splitnama[-1][0].title())

# 5) Faktorial

number = int(input('Masukkan angka: '))
hasil = 1
for i in range(1, number + 1):
    hasil = hasil * int(i)
print(f'{number}! = {hasil}')

# alternatif algoritma menggunakan while loop

value=int(input("Masukkan angka: "))
i=1
faktorial=1

while i<=value:
    faktorial*=i
    i+=1

print("Faktorial dari", value, "adalah", faktorial)
