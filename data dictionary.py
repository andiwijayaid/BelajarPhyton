# dictionary

mahasiswa1 = {"Nama":"Andi Wijaya",
              "NIM":"D42116516",
              "Prodi":"Teknik Informatika",
              "Tanggal Lahir":"25/08/1998",
              "Umur":19}

mahasiswa2 = {"Nama":"Santoso Aji",
              "NIM":"D42116520",
              "Prodi":"Ilmu Hukum",
              "Tanggal Lahir":"01/01/1999",
              "Umur":19}

print(mahasiswa1)
print("")
print("Nama Mahasiswa:", mahasiswa1["Nama"]) # Nomor Index diganti dengan key
print("NIM Mahasiswa:", mahasiswa1["NIM"])
print("Usia:", mahasiswa1["Umur"], "tahun")

print("")
print(mahasiswa1.keys()) # Mencetak key dari objek mahasiswa1
print(mahasiswa1.values()) # Mencetak values dari objek mahasiswa1

print("")
print(100*"_")
print("Kegunaannya bisa jadi seperti database no SQL")
mahasiswa = {"D42116516":mahasiswa1, "D42116520":mahasiswa2}
print(mahasiswa["D42116516"])