from array import *
def printArray(array):
    index = 0
    print("Array is: [", end='')
    for a in array:
        if index == len(array) - 1:
            print(f"{a}", end='')
            break
        else:
            print(f"{a}, ", end='')
            index+=1
    print("]\n")

#array adalah data struktur yang membuat list, sets, tuple, dictionary.
#array berfungsi sama seperti list, tetapi ia tak bisa mengandung 2 tipe variabel berbeda
#untuk membuat array kita harus import array library
#Daftar parameter
#b = int
#B = int
#u = char
#h = int
#H = int
#i = int
#I = int
#l = int
#L = int
#q = int
#Q = int
#f = float
#d = float
#Source: https://www.geeksforgeeks.org/python-arrays/
#array syntax

a = array('i', [1, 2, 3, 4, 5, 6]) #namaVariabel = array('masukan kode', [masukan data])

#untuk print array kita menggunakan for loop

for numbers in a:
    print("Numbers:",numbers)
    
#untuk menambahkan elemen baru kita menggunakan append function
print("Before append")
printArray(a)

a.append(10)
print("After append")
printArray(a) #using function

#kita juga bisa menggunakan insert function 
print("Before insert: ")
printArray(a)
a.insert(5, 44) #namaVariavel.insert(masukanIndexSesudah, masukanData)
print("After insert: ")
printArray(a)

#untuk menghapus data pada array python kita bisa menggunakan
#del function
print("Before del function")
printArray(a)
del a[2] #del arrayVariabel[index]  

print("Setelah del function")
printArray(a) #index ke 2 yaitu angka 3 telah dihapus

#pop function
#pop function fungsinya sama seperti pop function list

print("Before pop function")
printArray(a) 
b = a.pop(0) # mengeluarkan data di array a pada index ke 0 dan memasukannya ke variabel b
print("Setelah pop function")
printArray(a)
print(f"Angka yang dikeluarkan: {b}\n")

##remove function, data dengan memasukan datanya secara langsung
print("Before remove function")
printArray(a)
a.remove(4) #arrayVariabel.remove(masukan data yang ingin dihapus)
print("setelah remove function")
printArray(a)

#lalu terakhir del function bisa juga dipakai untuk menghapus seluruh data array
del a #del masukanNamaArray

try:
    printArray(a)
except:
    print("Array tersebut tidak ada")
