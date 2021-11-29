from typing import List


def showHeader(namaFunction):
    print("======== ", namaFunction , " Function ========\n")

#List adalah struktur data pada pyhton yang bisa menyimpan berbagai macam tipe data.
#list juga dapat merubah tipe data pada data yang ada di struktur tersebut.
#cara membuat list adalah dengan cara berikut
#nama variabel = [isi data]


list1 = [1, 2, 3]
list2 = [1, 1.3 , "Raihan", True] #list bisa menyimpan berbagai macam tipe data

#Untuk menambahkan data ke list terdapat 3 method yaitu 
#append, extend, insert

showHeader("Append")
#append function berfungsi untuk menambahkan elemen data baru ke bagian akhir list
list1.append("Budi") # menambahkan string baru ke list1
print(list1, "\n")

showHeader("Extend")
#extend function berfungsi untuk menambahkan list atau data struktur satu ke data struktur lainnya
list1.extend(list2) # extends akan menambahkan list2 ke list1 pada bagian akhir list1
print(list1, "\n")

showHeader("Insert")
#insert function berfungsi untuk menambahkan elemen data ke list pada index atau lokasi yang spesifik
list1.insert(0, "Index pertama")
print(list1 , "\n")

listBaru = [1, 2 , 3, 4, 5]

#untuk menghapus elemen pada list terdapat beberapa function yang bisa digunakan yaitu
# del, pop(), dan remove()

#del function berfungsi mendelet elemen data pada index tertentu, atau dari index 1 sampai ke n pada list
#del function hanya berfungsi untuk menghapus data tidak mengembalikannya
showHeader("Del")
del listBaru[0] #menghapus elemen pada index ke 0
print(listBaru , "\n")

del listBaru[2:4] #menghapus elemen pada index ke n sampai ke n - 1
print(listBaru, "\n")







