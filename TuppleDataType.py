from ListData import *

#tupple adalah tipe data struktur yang fugsinya sama seperti list.
#yang membedakan adalah data pada tupple tidak dapat dirubah
showHeader("Akses tuple")
tuple1 = (1, 2, 3, 4, 5 ,6 ,7 ,8, 9)
print(tuple1) #mengakses tuple dengan print
print(tuple1[0]) #mengakses tuple index ke 0
print(tuple1[0:3]) # mengakses tuple index ke 0 sampa ke n - 1
print(tuple1[0:5:2], "\n") # mengakses tuple index ke 0 sampai n - 1 dengan beda 2

