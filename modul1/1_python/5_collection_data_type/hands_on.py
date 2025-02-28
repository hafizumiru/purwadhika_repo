listContoh = ['hello', 1, 1, 3, True]

# print(listContoh[0]) # ['hello']
# print(listContoh[3]) # [3]
# print(listContoh[1:4]) # [1, 1, 3]
# print(listContoh[-4:-1]) # [1, 1, 3]
# print(listContoh[0:-2]) # ['hello', 1, 1]
# print(listContoh[:-3]) # ['hello', 1]
# print(listContoh[-2:]) # [3, True]
# print(listContoh)

listContoh[1] = 'test'
listContoh[-2] = 'tist'

# print(listContoh)

listContoh.append('coba')
listContoh.insert(1, 'gblh')

# print(listContoh)

# listContoh[4] = 'test'
# print(listContoh)
# listContoh.remove('test') # hapus string test pada index ke 2
# print(listContoh)
# listContoh.pop() # hapus data index terakhir (string coba)
# print(listContoh)
# del listContoh[4] # hapus True
# print(listContoh)
# listContoh.clear() # hapus semua data di list
# print(listContoh)
# print(type(listContoh)) # <class 'list'>
# for item in listContoh:
#     print(type(item))

# if 'tist' in listContoh:
#     print(len(listContoh))
# else:
#     print('Eksekusi Mati')

# print(listContoh)

newList1 = listContoh
newList1[1] = 'contoh'

newList2 = listContoh.copy()
newList2[2] = 'baru'

# print(newList1)
# print(newList2)
# print(listContoh)

indexDicari = listContoh.index(bool('True'))
# print(indexDicari)

listContoh1 = ['charlie', 'budi', 'لا', '1', '3', '2', 'arie', 'sutaryadi', 'subianto', 'fufufafa']
listContoh1.sort(reverse = False)
# print(listContoh1)
listContoh1.reverse()
# print(listContoh1)

myDict = {
    'nama': 'Budi',
    'usia': 25,
    'pekerjaan': 'Judi',
    'menikah': False,
}
# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())

# for key,val in myDict.items():
#     print(f'{key} = {val}')

if 'kelamin' in myDict:
    print('Udah punya kelamin')
else:
    myDict['kelamin'] = 'Pria Punya Selera'
# print(myDict)

setContoh = {'Fast n Furious', '2 Fast 2 Furious', 'Fast n Furious: Tokyo Drift'}

setContoh.add('Fast 8')

setContoh.update(['Furious 9', 'The Fast n The Furious'])
print(setContoh)

setContoh.remove('Hobbs n Shaw')