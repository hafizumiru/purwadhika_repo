# 1

# list = [5, 6, 3, -1, -3, 5]


# def avg(list):
#     avg = 0
#     for i in list:
#         avg += i
#     avg /= len(list)
#     return avg


# print(avg(list))

# 2

def gcd(a, b):
    while b != 0:
        temp = a 
        a = b 
        b = temp % b

    if a == 1:
        return 
    else:
        return {a}

print(gcd(15, 25))


# 3


# def isLeapYear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False


# while True:
#     try:
#         year = int(
#             input("Masukan tahun (masukan 0 untuk menghentikan program): "))
#         if year == 0:
#             break
#         else:
#             print(f"is {year} Leap Year? {isLeapYear(year)}")
#     except:
#         print("Tolong masukan hanya tahun!")

# 4
