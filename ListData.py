#List adalah struktur data pada pyhton yang bisa menyimpan berbagai macam tipe data.
#list juga dapat merubah tipe data pada data yang ada di struktur tersebut.
#cara membuat list adalah dengan cara berikut
#nama variabel = [isi data]


list1 = [1, 2, 3]
list2 = [1, 1.3 , "Raihan", True] #list bisa menyimpan berbagai macam tipe data

#Untuk menambahkan data ke list terdapat 3 method yaitu 
#append, extend, insert

#append function berfungsi untuk menambahkan elemen data baru ke bagian akhir list
list1.append("Budi") # menambahkan string baru ke list1
print(list1)

#extend function berfungsi untuk menambahkan list atau data struktur satu ke data struktur lainnya
list1.extend(list2) # extends akan menambahkan list2 ke list1 pada bagian akhir list1
print(list1)

#insert function berfungsi untuk menambahkan elemen data ke list pada index atau lokasi yang spesifik
list1.insert(0, "Index pertama")
print(list1)




