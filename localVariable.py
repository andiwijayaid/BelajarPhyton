# Local
namaPemain = "Zlatan"

def jualStriker(strikerBaru):
    namaPemain = strikerBaru
    print("Pemain saya adalah", namaPemain)

jualStriker("Lukaku")
print("Pemain saya adalah", namaPemain)

print(30*'=')
print('')

# Global
namaPemain = "Zlatan"

def jualStriker(strikerBaru):
    global namaPemain # add as many global var as you want, seperated with ','
    namaPemain = strikerBaru
    print("Pemain saya adalah", namaPemain)

jualStriker("Lukaku")
print("Pemain saya adalah", namaPemain)