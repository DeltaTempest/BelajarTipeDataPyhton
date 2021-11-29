from typing import List


def showHeader(namaFunction):
    print("======== ", namaFunction , " ========\n")

#List adalah struktur data pada pyhton yang bisa menyimpan berbagai macam tipe data.
#list juga dapat merubah tipe data pada data yang ada di struktur tersebut.
#cara membuat list adalah dengan cara berikut
#nama variabel = [isi data]


list1 = [1, 2, 3,4,5,6,7,8,9]
list2 = [1, 1.3 , "Raihan", True] #list bisa menyimpan berbagai macam tipe data

#Untuk mengaksesnya bisa dengan cara berikut
print(list1) #printnya secara langsung secara keseluruhan
print(list1[0]) #print index nya secara spesifik
print(list1[0:3]) #print dari index ke 0 sampai n-1
print(list1[0:6:2]) #print dri index ke 0 sampai index ke n - 1 dengan beda 2


#Untuk menambahkan data ke list terdapat 3 method yaitu 
#append, extend, insert

showHeader("Append Function")
#append function berfungsi untuk menambahkan elemen data baru ke bagian akhir list
list1.append("Budi") # menambahkan string baru ke list1
print(list1, "\n")

showHeader("Extend Function")
#extend function berfungsi untuk menambahkan list atau data struktur satu ke data struktur lainnya
list1.extend(list2) # extends akan menambahkan list2 ke list1 pada bagian akhir list1
print(list1, "\n")

showHeader("Insert Function")
#insert function berfungsi untuk menambahkan elemen data ke list pada index atau lokasi yang spesifik
list1.insert(0, "Index pertama")
print(list1 , "\n")

listBaru = [1, 2 , 3, 4, 5]

#untuk menghapus elemen pada list terdapat beberapa function yang bisa digunakan yaitu
# del, pop(), dan remove()

#del function berfungsi mendelet elemen data pada index tertentu, atau dari index 1 sampai ke n pada list
#del function hanya berfungsi untuk menghapus data tidak mengembalikannya
showHeader("Del Function")
del listBaru[0] #menghapus elemen pada index ke 0
print(listBaru , "\n")

del listBaru[2:4] #menghapus elemen pada index ke n sampai ke n - 1
print(listBaru, "\n")

showHeader("Pop Function")
#Pop function berfungsi untuk menghapus atau mengembalikan elemen data pada list secara spesifik

listNama = ["Raihan", "Awang", "Budi"]
print("Elemen yang dihilangkan:",listNama.pop(1), "\n") #dia akan mengembalikan elemen pada index pertama dan menghapusnya dari list 

print("List nya sekarang",listNama, "\n")

showHeader("Remove Function")
#Seperti namanya remove function berfungsi untuk menghapus elemen data yang spesifik pada list. Remove di tentukan bukan oleh index

listBuah = ['mangga', 'apel', 'pisang']
listBuah.remove('mangga') # menghapus elemen pisang pada listBuah
print("ListBuah: ", listBuah, "\n")








