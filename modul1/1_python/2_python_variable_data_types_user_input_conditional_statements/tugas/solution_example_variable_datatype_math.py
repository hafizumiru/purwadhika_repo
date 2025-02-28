# Contoh Solusi Exercise Data Types, Variable & Math Operations

# 1 
# Function
x = int(input("Masukkan nilai x: ")) # 4
y = int(input("Masukkan nilai y: ")) # 3
z = int(input("Masukkan nilai z: ")) # 2

print(( (x + (y * z)) / (x * y)) ** 2)

# 2 
# Rasio usia Andi dan Budi

# Algoritma :
# A+B = 49
# A/B = 0.4
# A = 0.4B

# 0.4B + B = 49
# 1.4B = 49
# B = 49/1.4
# B = 35

# A = 35*0.4
# A = 14

# A+2 = 14+2 = 16
# B+2 = 35+2 = 37

totalUsia = 49
rasioUsia = 0.4

usiaBudi = totalUsia / (1+rasioUsia)
usiaAndi = usiaBudi * rasioUsia
print('')
print(f'(5) Usia Andi 2 Tahun kemudian adalah : {int(usiaAndi)+2} dan Usia Budi adalah : {int(usiaBudi)+2}')
print('')

# 3
# Mobil A dan B nabrak

# Rumus Jarak :
# jarak = kecepatan*waktu

# Algoritma : 

# Jarak Mobil A :
# jarakA = kecepatan*waktu
# jarakA = 60*t

# Jarak Mobil B : 
# jarakB = kecepatan*waktu
# jarakB = 40*t

# Total Jarak = 120
# jarakA + jarakB = 120
# 60t + 40t = 120
# 100t = 120
# t = 120/100
# t = 1.2 jam
# t = 1.2*60
# t = 72

# Waktu tabrakan : 
# waktu berangkat + waktu kedua mobil bertemu
# 09.00 + 72 menit = 10.12

jarak = 120
kecepatanA = 60
kecepatanB = 40
jamAwal = 9
menitAwal = 0
waktuTabrakan = jarak / (kecepatanA+kecepatanB)
jamTabrakan = int(waktuTabrakan + jamAwal)
menitTabrakan = int((waktuTabrakan*60)%60)

print(f'(6) Kedua Mobil akan bertabrakan pada Pukul {jamTabrakan}.{menitTabrakan}')

# 4
# Toko buah

hargaApel = 10000
hargaJeruk = 15000
hargaAnggur = 20000

jumlahApel = int(input('Masukkan Jumlah Apel : ')) # 2
jumlahJeruk = int(input('Masukkan Jumlah Jeruk : ')) # 3
jumlahAnggur = int(input('Masukkan Jumlah Anggur : ')) # 5

totalHargaApel = jumlahApel * hargaApel
totalHargaJeruk = jumlahJeruk * hargaJeruk
totalHargaAnggur = jumlahAnggur * hargaAnggur

print('''
Detail Belanja

Apel : {jmlApel} x {hrgApel} = {totalHrgApel}
Jeruk : {jmlJeruk} x {hrgJeruk} = {totalHrgJeruk}
Anggur : {jmlAnggur} x {hrgAnggur} = {totalHrgAnggur}

Total : {totalHarga}
'''.format(jmlApel=jumlahApel, hrgApel=hargaApel, totalHrgApel=totalHargaApel, 
    jmlJeruk=jumlahJeruk, hrgJeruk=hargaJeruk, totalHrgJeruk=totalHargaJeruk,
    jmlAnggur=jumlahAnggur, hrgAnggur=hargaAnggur, totalHrgAnggur=totalHargaAnggur,
    totalHarga=(totalHargaAnggur+totalHargaApel+totalHargaJeruk)))

# 5
# Mencari kuadrat
number = input("Masukan angka: ")
result = int(number) ** 2
print(f"Kuadrat dari {number} adalah {result}")

# 6
# Walter White x Willy Wonka
mesinA = 5000
mesinB = 7500
mesinC = 3500
hasil_sehari = 7 
hasil_sebulan = 25 

pabrik_btm = (int((mesinA * 5) + (mesinB * 2)) * hasil_sehari * hasil_sebulan)
pabrik_jkt = (int((mesinB * 3) + (mesinC * 7)) * hasil_sehari * hasil_sebulan)

print(f"Hasil sebulan parbrik Batam: {pabrik_btm} dan Hasil sebulan pabrik Jakarta: {pabrik_jkt}")
print(("Hasil Penjumlahan dari pabrik Batam dan Pabrik Jakarta adalah :"), pabrik_btm + pabrik_jkt)

# 7
# Hitung konversi tahun, bulan, minggu dan hari

jumlah_hari = int(input("Masukkan Jumlah hari: ")) # 400
# Jumlah Hari di floor division dengan 360 untuk mendapatkan Tahun
tahun = jumlah_hari // 360
# Sisa Hari di modulus dengan 365 untuk mendapatkan sisa bagi
sisa_tahun = int(jumlah_hari) % 360
# Sisa bagi tahun di floor division dengan 30 untuk mendapatkan Bulan
bulan = sisa_tahun // 30
# Sisa bagi bulan di modulus dengan 30 untuk mendapatkan sisa bagi
sisa_bulan = sisa_tahun % 30
# Sisa bagi bulan di floor division dengan 7 untuk mendapatkan Minggu
minggu = sisa_bulan // 7
# Sisa bagi minggu di modulus dengan 7 untuk mendapatkan Hari
hari = sisa_bulan % 7
# Menampilkan Output
print (tahun, "Tahun", bulan,"Bulan", minggu,"Minggu", hari,"Hari")
# 1 tahun 1 bulan

