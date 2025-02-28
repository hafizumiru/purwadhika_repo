import math as meth

nama = 'Hardiv'
nama = 'Nugraha'
# print(nama)

# print('Terima kasih sudah datang')
# print('Terima kasih sudah datang')
# print('Terima kasih sudah datang')

ucapan = 'Terima kasih atas kerjasamanya'
# print(ucapan)
# print(ucapan)
# print(ucapan)

umur = 99
umur = 99.99
ucapan = 'saya bund\'ar\bsaya juga'
greetings = '''dilan berkata,"I'm gay"'''
posisiKoma = greetings.index(',')

# print(greetings.capitalize())
# print(greetings[-4:-2])

angka1 = 12
# print(type(angka1)) # int
angka1 = str(angka1)
# print(type(angka1)) # str
angka2 = "12"
# print(type(angka2)) # str
angka2 = float(angka2)
# print(type(angka2)) # int

x = True
# print(type(x))
y = 'True'
# print(type(y))

x = 5 # 5
x += 3 # x = x + 3 # 8
x -= 3 # x = x - 3 # 5
x *= 3 # x = x * 3 # 15
x /= 3 # x = x / 3 # 5
x %= 3 # x = x % 3 # 2
x //= 3 # x = x // 3 # 0
x **= 3 # x = x ** 3 # 0.0
# print(x)

# print(meth.pow(meth.pi,2))

# print("Apel " + str(5))

txt = 'Is{angka3} saya {jumlahIstriIdeal}'
num = 3
jumlahIstri = 1
# print(txt)
# print(txt.format(jumlahIstriIdeal = jumlahIstri, angka3 = num))
# print(txt)
txt = txt.format(jumlahIstriIdeal = jumlahIstri, angka3 = num)
x = 'jumlah' in txt
# print(x)

# username = input("Masukkan Username anda: ")
# umur = input("Masukkan umur anda: ")
# print('Username anda adalah ' + username + ' dan umur anda ' + umur + ' tahun')

a = 20
b = 20

# print(a < b and b > a) # FALSE

umurPemohon = int(input("Masukkan umur anda sebagai syarat membuat SIM: "))

# 17-100: Lulus : 17 <= umur <= 100
# 0-16: Gak lulus
# > 100: Ketuaan

if umurPemohon >= 17 and umurPemohon <= 100:
    print("Selamat, anda lulus screening!\nSilahkan buka email anda untuk melihat link tes")
elif umurPemohon >= 0 and umurPemohon < 17:
    print("Mohon maaf pengajuan anda ditolak!\nUmur anda masih belum memenuhi standar")
elif umurPemohon < 0:
    print("Belom lahir")
else:
    print("Antara lu udah ketuaan atau udah jadi hantu")

f = 80
g = 80.1