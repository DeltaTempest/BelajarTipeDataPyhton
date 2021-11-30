from ListFungsi import *

#sets adalah koleksi atau data struktur yang tidak teratur, yang terdiri dari berbagai macam elemen unik, dan datanya tidak bisa dirubah
#tidak teratur berarti kita tidak bisa mengakses secara index spesifik terhadap value sets
#selain itu sets tidak bisa memiliki 2 variabel yg sama persis
#sets syntax
#NamaVariabel = {masukan elemen}

sets1 = {1, 2, 3, 4, "herwin"}

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




