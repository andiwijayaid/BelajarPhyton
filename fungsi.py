#Simple function without argument
def function():
    print('ini fungsi')
function()

print(30*'=')
print('')

#Function with argument
def suaraAyam(suara):
    print(suara)

def hargaAyam(harga):
    suaraAyam("kukuruyuk")
    print("Harga ayam adalah Rp", harga)

hargaAyam(20000)

print(30*'=')
print('')

#Function with multiple argument
def myTeacher(nama, age, pelajaran, status):
    print("My teacher name is", nama, ",", age, "years old. "
          "She is a", pelajaran, "teacher. ",
          "She is also my", status, ".")

myTeacher("Dewianti", 25, "Art", "Academic Counselors")

print(30*'=')
print('')

#Function with return value
def returnValueFunction():
    a = 1+1
    return a

print(returnValueFunction())