import math

# # 1

# list = [23, 57, 76, 6, 60, 28, 30,
#         44, 85, 44, 97, 32, 71, 85,
#         46, 95, 29, 37, 13, 79, 15, 9,
#         23, 10, 22, 78, 46, 2, 99, 3]

# terkecil = 0
# terbesar = 0

# for index in range(len(list)):
#     if list[terkecil] > list[index]:
#         terkecil = index
#     if list[terbesar] < list[index]:
#         terbesar = index

# print(f"Max number: {list[terbesar]}\nMin number: {list[terkecil]}")

# # 2

# list = [
#     'K0QY6', 'fJU08', 'K0QY6', 'VeZrS', 'jxjQ6', 'sjqom', 'AefAN', 'jxjQ6',
#     'S90wn', 'FZw7F', 'IgYbm', 'dD1ZM', 'sjqom', 'dD1ZM', 'fJU08', 'AefAN',
#     'jxjQ6', 'K0QY6', 'prdDz', 'dD1ZM', 'AefAN', 'WfgpU', 'VeZrS', 'sjqom'
# ]
# setList = set(list)

# print(f"Terdapat ID unik sebanyak: {len(setList)}")

# # 3

# list = [
#     344, 838, 502, 262, 590, 959, 151, 491, 71, 980, 156, 13, 280, 615, 278, 185,
#     851, 599, 947, 598, 961, 534, 633, 751, 836, 446, 7, 956, 335, 765, 600, 428,
#     595, 478, 667, 628, 375, 402, 663, 728, 704, 182, 377, 380, 49, 253, 566,
#     662, 492, 930, 285, 5, 467, 496, 421, 317, 774, 86, 942, 149, 270, 765, 357,
#     373, 336, 63, 976, 509, 863, 139, 504, 321, 635, 96, 977, 538, 552, 683, 83,
#     752, 576, 350, 538, 79, 164, 414, 579, 948, 971, 121, 354, 562, 562, 63, 385,
#     185, 731, 872, 342, 898
# ]

# square_number_list = []

# for angka in list:
#     if math.sqrt(angka) == int(math.sqrt(angka)):
#         square_number_list.append(angka)

# print(f"Total square number: {len(square_number_list)}\n{square_number_list}")

# # 4

# me = input("Masukan film favoritmu: ")
# friend = input("Masukan film favorit temanmu: ")
# my_favorite_film = set(me.replace(" ", "").replace("'", "").lower().split(","))
# friend_favorite_film = set(friend.replace(
#     " ", "").replace("'", "").lower().split(","))

# film_sama = my_favorite_film.intersection(friend_favorite_film)
# film_gabung = my_favorite_film.union(friend_favorite_film)

# similarity_level = (len(film_sama)/len(film_gabung))*100

# print(f"Similarity level {similarity_level:.2f}%")

# 5

menu = 0

print(
'''
Selamat Datang di Pasar Buah

List Menu:
1. Menampilkan Daftar Buah
2. Menambah Buah
3. Menghapus Buah
4. Membeli Buah Buah
5. Exit Program
''')


# 6
