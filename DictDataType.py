from ListFungsi import *  

#Dictionary atai dict adalah data struktur yang memiliki key dan value
#data pada dict tidak bisa dirubah rubah
#cara penulisan
showHeader("Membuat Dictionary")
dict1 = {"Tempest" : "Suka makan apel",
         "Rimuru" : "Adalah slime"
         }
#Disini Tempest, dan Rimuru adalah key, dan "suka makan apel" dan "Adalah slime" adalah value
showHeader("Mengakses Dictionary")
print(dict1["Rimuru"]) # mengakses value yang ada di dalam "rimuru"
print(dict1.keys(), "\n") # menampilkan list keys yang ada di dictionary

showHeader("Merubah value pada dictionary")
dict1["Rimuru"] = "Adalah monster" # merubah value pada "rimuru"
print("RImuru: ",dict1["Rimuru"], "\n")

