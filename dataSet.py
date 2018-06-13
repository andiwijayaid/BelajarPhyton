print("Data set adalah himpunan yang sering kita kenal dalam matematika")
set = {1,2,3,4,5,6,7}
print(set)
print("")

print("Tambah", 5)
print(set)
set.add(5)
print("Data di atas tidak berubah karena set akan menganggap data 5 adalah sama")

set.add(10)
print(set)

print("")
print(100*'_')

ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print("Data set mendukung fitur gabung dan intersect")
print(ganjil)
print(genap)
print(prima)
print("")
print("Ganjil gabung genap:", ganjil.union(genap))
print("Ganjil intersect prima:", ganjil.intersection(prima))
