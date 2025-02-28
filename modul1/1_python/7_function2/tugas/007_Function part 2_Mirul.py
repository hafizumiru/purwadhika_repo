# def fact(angka):
#     if angka <= 0:
#         print("Angka yang anda masukan tidak valid")
#     else:
#         fact = 1
#         for i in range(1, angka + 1):
#             fact *= i
#         return fact


# print(fact(3))

# list1 = [1, 3, 4, 5]
# list2 = [22, 17, 19, 20, 14]
# list3 = [1, 3, 5]
# list4 = [2, 4, 6]


# def mapping(list):
#     transformlist = ["Genap" if i != 0 and i %
#                      2 == 0 else "Ganjil" for i in list]
#     return transformlist


# print(mapping(list1))
# print(mapping(list2))
# print(mapping(list3))
# print(mapping(list4))

# gaji = [9100000, 9800000, 9500000, 10300000, 9300000]


# def filter(list):
#     result = [i for i in list if i - (i * 5 / 100) >= 9000000]
#     return result


# print(filter(gaji))
