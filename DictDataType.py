from ListFungsi import *  

#Dictionary atai dict adalah data struktur yang memiliki key dan value
#data pada dict tidak bisa dirubah rubah
#cara penulisan
#namaVariabel = {key : value}

dict1 = {"Tempest" : "Suka makan apel",
         "Rimuru" : "Adalah slime"
         }
#Disini Tempest, dan Rimuru adalah key, dan "suka makan apel" dan "Adalah slime" adalah value
showHeader("Mengakses Dictionary")
#mengakses dictionary bisa dilakukan dengan syntax namaVariabel[key]

print("Rimuru: ",dict1["Rimuru"]) # mengakses value yang ada di dalam "rimuru"
print(dict1.keys(), "\n") # menampilkan list keys yang ada di dictionary
print(dict1.items(), "\n") # menampilkan list value dan key

showHeader("Merubah value pada dictionary")
print("Sebelum dirubah: ", dict1["Rimuru"])
#merubah value pada dictionary dapat dilakukan dengan syntax namaVariabel[key] = masukan value baru
dict1["Rimuru"] = "Adalah monster" # merubah value pada key "rimuru"
print("Sesudah dirubah: ",dict1["Rimuru"], "\n") #print key "rimuru"

showHeader("Menambahkan key dan value baru")
#menambahkan key dan value baru bisa dilakukan dengan syntax namaVariabelDict[key baru] = value baru
print("Sebelum menambahkan key dan value baru\n", dict1)
dict1["Diablo"] = "Adalah bawahan rimuru"
print("Setelahnya\n", dict1)

showHeader("Menghapus data pada dictionary")
print("Sebelum dihapus:\n", dict1)
#berikut adalah function untuk menghapus data pada dict

#del function, syntax = del = namaVariabel[key]
del dict1["Diablo"]
print("Setelah dihapus menggunakan del:\n", dict1, "\n")
dict1["Diablo"] = "Adalah bawahan rimuru"

#pop() dan popItem() function
#pop function berfungsi untuk mengembalikan nilai value dict lalu menghapus key dan valuenya pada dictionary tersebut

dict2 = dict1.pop("Rimuru")

print("Dict1:\n", dict1, "\n")
print("dict2:\n",dict2, "\n")

#popItem berfungsi sama seperti pop, tetapi ia melakukan operasinya pada key dan value yang terakhir dan ia mengembalikan key dan value

dict3 = dict1.popitem()

print("Dict1:\n", dict1, "\n")
print("dict3:\n",dict3, "\n")


