import sys
import timeit

dataTuple = (1,2,3,4,5,6) #tipe data sama dengan list tapi isinya fix dan tidak bisa ditambah/dikurang
dataList = [1,2,3,4,5,6]

print(dataTuple)


besar_dataTuple = sys.getsizeof(dataTuple) # tuple punya ukuran yang lebih kecil
besar_dataList = sys.getsizeof(dataList)

print("besar data tuple: ", besar_dataTuple)
print("besar data list: ", besar_dataList)

waktu_dataTuple = timeit.timeit(stmt="(1,2,3,4,5,6)", number=1000000) # waktu eksekusi tuple lebih cepat dibandingkan list
waktu_dataList = timeit.timeit(stmt="[1,2,3,4,5,6]", number=1000000) # ini karena tuple tidak menampung informasi method hapus dan tambah

print("lama proses tuple: ", waktu_dataTuple)
print("lama proses list: ", waktu_dataList)