import math

# 1 Clear

# x = 4
# y = 3
# z = 2

# result = math.pow((x+(y*z))/(x*y),2)
# print(result)

# 2

# # Andi+Budi = 49
# # Andi/Budi = 0.4
# # Andi = 0.4Budi

# # 0.4Budi + Budi = 49

# # 1.4Budi = 49

# budi = 49/1.4 = 35
# andi = 0.4 * 35 = 14

# # Andi dan Budi 2 tahun lagi
# andi = andi + 2 = 16
# budi = budi + 2 = 37 

# print("Umur Andi 2 tahun lagi adalah " + str(andi) +" Tahun")
# print("Umur Budi 2 tahun lagi adalah " + str(budi) +" Tahun")


# 3 Clear

# kecepatan_gabungan = 100
# jarak_total = 120

# jam = 9

# tabrakan = jarak_total/kecepatan_gabungan

# jam += tabrakan
# menit = (jam -(math.floor(jam)))
# jam = math.floor(jam)
# menit = math.ceil(60*menit)

# print("Mobil akan bertabrakan pada pukul "+ str(jam) +":"+ str(menit)+" WIB") 

# 4 Clear

# apel = int(input("Masukan Jumlah Apel: "))
# jeruk = int(input("Masukan Jumlah Apel: "))
# anggur = int(input("Masukan Jumlah Apel: "))

# total_apel = apel * 10000
# total_jeruk =  jeruk * 15000
# total_anggur = anggur * 20000

# total_belanja = total_apel + total_jeruk + total_anggur

# print("Detail Belanja")
# print("Apel : "+str(apel)+" x 10000 = " + str(total_apel))
# print("Apel : "+str(jeruk)+" x 10000 = " + str(total_jeruk))
# print("Apel : "+str(anggur)+" x 10000 = " + str(total_anggur))
# print("Total : "+ str(total_belanja))

# 5 Clear

# angka = int(input("Silahkan masukan angka berapapun: "))
# kuadrat = math.pow(angka,2)
# print("Kuadrat dari "+ str(angka) +" = "+ str(kuadrat))

# 6 Clear
 
# mesin_a = 5000
# mesin_b = 7500
# mesin_c = 3500

# pabrik_a = (5*mesin_a)+(2*mesin_b)
# pabrik_b = (3*mesin_b)+(7*mesin_c)

# permen_perhari = (pabrik_a + pabrik_b)*7
# permen_perbulan = permen_perhari*25

# print("Permen yang dihasilkan selama sebulan adalah "+ str(permen_perbulan) +" permen")

# 7 Clear

# hari = int(input("Masukan berapa hari:"))
# tahun = math.floor(hari/360)
# hari = hari - (tahun*360)
# bulan = math.floor(hari/30)
# hari = hari - (bulan*30)
# minggu = math.floor(hari/7)
# hari = hari - (minggu*7)
# print(str(tahun)+" Tahun " +str(bulan)+" Bulan " +str(minggu)+" Minggu " +str(hari)+" Hari")

# 8 Clear

# number = int(input("Masukan Angka: "))
# if number%2 == 1:
#     print("Number "+str(number)+" is odd")
# elif number%2 == 0:
#     print("Number "+str(number)+" is even")

# 9 Clear

# info = ""
# massa = int(input("Masukan Massa (kg) : "))
# tinggi = int(input("Masukan Tinggi (cm) : "))/100
# imt= massa/(math.pow(tinggi,2))

# if imt < 18.5:
#     info ="BERAT BADAN KURANG!"
# elif imt >= 18.5 and imt < 25:
#     info = "BERAT BADAN IDEAL!"
# elif imt >= 25 and imt < 30:
#     info = "BERAT BADAN BERLEBIHAN!"
# elif imt >= 30 and imt < 40:
#     info = "BERAT BADAN SANGAT BERLEBIHAN!"
# else:
#     info = "OBESITAS!"

# print("Massa "+str(massa)+" kg dan tinggi " +str(tinggi)+" m")
# print("IMT = "+ str(imt) + " " +info)

# 10 Clear

# apel = int(input("Masukan Jumlah Apel: "))
# jeruk = int(input("Masukan Jumlah Apel: "))
# anggur = int(input("Masukan Jumlah Apel: "))

# total_apel = apel * 10000
# total_jeruk =  jeruk * 15000
# total_anggur = anggur * 20000

# total_belanja = total_apel + total_jeruk + total_anggur

# print("Detail Belanja")
# print("Apel : "+str(apel)+" x 10000 = " + str(total_apel))
# print("Apel : "+str(jeruk)+" x 10000 = " + str(total_jeruk))
# print("Apel : "+str(anggur)+" x 10000 = " + str(total_anggur))
# print("Total : "+ str(total_belanja))

# bayar = int(input("Masukan jumlah uang : "))
# if bayar < total_belanja:
#     print("Transaksi anda dibatalkan\nuangnya kurang sebesar "+ str(total_belanja - bayar))
# elif bayar == total_belanja:
#     print("Terimakasih")
# elif bayar > total_belanja:
#     print("Terimakasih\nUang kembali anda : "+ str(bayar - total_belanja))