from ListFungsi import *

#sets adalah koleksi atau data struktur yang tidak teratur, yang terdiri dari berbagai macam elemen unik, dan datanya tidak bisa dirubah
#tidak teratur berarti kita tidak bisa mengakses secara index spesifik terhadap value sets
#selain itu sets tidak bisa memiliki 2 variabel yg sama persis
#sets syntax
#NamaVariabel = {masukan elemen}

sets1 = {1, 2, 3, 4}

showHeader("Mengakses sets")
#sets hanya bisa diakses secara keseluruhan tidak bisa satu persatu
print(sets1) #print sets1

showHeader("Menambahkan elemen baru")
#untuk menambahkan elemen baru pada sets bisa dilakukan dengan cara berikut
#namaSets.add(masukan elemen data)
sets1.add(5)
sets1.add(5)
print(sets1)

#tidak hanya itu fungsi set juga bisa digunakan untuk membuat set baru dari iterable lainnya
listAngka = [3, 1,5,9,2, 7, 5, 10, 11, 1] #angka tak beraturan dan berduplikat
print("set angka sebelumnya(list): ", listAngka)
setAngka = set(listAngka) # menjadi teratur dan tidak berduplikat
print("Set angka baru(sets): ", setAngka)


showHeader("Union Function")
#union() function
#syntax
#setsBaru = sets1.union(masukan sets lain)
setAngka.clear() #menghapus semua data pada sets
setAngka = {4, 5, 6, 7}
sets2 = sets1.union(setAngka) # menggabungkan 2 set ke dalam sets2
print(sets2)


showHeader("Intersection function")
#intersection berfungsi untuk menampilkan data potongan atau data yang sama diantara kedua sets, setelah 2 sets di union
setsAngka1 = {1, 2, 3, 4, 5, 6}
setsAngka2 = {3, 4, 5, 6, 7, 8}
setsAngka1.union(setsAngka2) # menyatukan 2 sets
print("Intersection: ",setsAngka1.intersection(setsAngka2)) # menjalankan intersection function


showHeader("Diffrence function")
#diffrence fungtion
#berfungsi untuk mengeluarkan elemen data yang sama pada dua sets yang telah di satukan
#lalu mengeluarkan elemen data sisanya hanya pada sets pertama

print("Diffrence: ",setsAngka1.difference(setsAngka2)) # dia akan me return 1, 2 karena hanya itu yang berbeda dan berada di sets 1

#symetric diffrence function 
#fungsinya sama seperti diffrence tetapi bedanya dia akan meng output kedua sets

print("Symetric diffrence", setsAngka1.symmetric_difference(setsAngka2)) # return 1 , 2, 7, 8





