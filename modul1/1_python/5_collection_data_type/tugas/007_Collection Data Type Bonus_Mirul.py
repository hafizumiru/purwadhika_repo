# 1

# sentence = "Aku baru makan nasi terus aku mau makan mie nanti malam"

# list_kata = sentence.lower().split()
# set_kata = set(list_kata)

# muncul = 0
# for kata_in_set in set_kata:
#     for kata_in_list in list_kata:
#         if kata_in_list == kata_in_set:
#             muncul += 1
#     print(f"{kata_in_set} muncul sebanyak {muncul} kali")
#     muncul = 0

# 2

# menu_daging = ["Ayam Panggang", "Ikan Bakar"]
# menu_sayuran = ["Sayuran Segar", "Sup Brokoli"]
# menu_kentang_nasi = ["Kentang Goreng", "Nasi Goreng"]
# menu_minuman = ["Air Mineral", "Jus Jeruk"]
# menu_hidangan_penutup = ["Puding Cokelat", "Cheesecake"]

# jumlah_menu = 1

# for i in range(len(menu_daging)):
#     for j in range(len(menu_minuman)):
#         for k in range(len(menu_kentang_nasi)):
#             for l in range(len(menu_hidangan_penutup)):
#                 if menu_daging[i].lower() == "ayam panggang" and menu_kentang_nasi[k].lower() == "kentang goreng":
#                     continue
#                 else:
#                     menu = [menu_daging[i], menu_minuman[j],
#                             menu_kentang_nasi[k], menu_hidangan_penutup[l]]
#                     print(f"Paket Makanan {jumlah_menu}: {menu}")
#                     jumlah_menu += 1

# for i in range(len(menu_sayuran)):
#     for j in range(len(menu_minuman)):
#         for k in range(len(menu_kentang_nasi)):
#             for l in range(len(menu_hidangan_penutup)):
#                 menu = [menu_sayuran[i], menu_minuman[j],
#                         menu_kentang_nasi[k], menu_hidangan_penutup[l]]
#                 print(f"Paket Makanan {jumlah_menu}: {menu}")
#                 jumlah_menu += 1
