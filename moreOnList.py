barang = ['kunci', 'ember', 'jaket', 'ban', 'mobil']

# Print list as array
print(barang)

# Add list data
barang.append('motor')
print(barang)

# Extend, menambahkan data satu persatu per karakter
barang.extend('dompet')
print(barang)

# Insert, memasukkan data pada index tertentu
barang.insert(0, "komputer")
print(barang)

# count, menghitung jumlah barang
barang.insert(5, "mobil")
jumlahMobil = barang.count("mobil")
print("jumlah mobil saya adalah", jumlahMobil)

# Remove, menghapus yang pertama ditemukan
barang.remove("mobil")
jumlahMobil = barang.count("mobil")
print("jumlah mobil saya adalah", jumlahMobil)

# Reverse, membalik urutan list
barang.reverse()
print(barang)
barang.reverse()
print(barang)

print(100*"=")

# Copy, mengambil isi array
stuff = barang.copy()
stuff.append("keyboard")
print("Stuff:", stuff)
print("Barang:", barang)

print("\n\t\t\t\t\t\t\t\t\t\tLihat perbedaanx\n")

# Kalau tidak pakai copy, maka barang akan mereferensi juga apa yang di tambahkan di var stuff
stuff = barang
stuff.append("keyboard")
print("Stuff:", stuff)
print("Barang:", barang)