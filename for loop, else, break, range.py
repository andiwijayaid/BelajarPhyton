
# Break
print("Break")
number = 25;
for i in range(10,50,5):
    if i is number:
        print(number, "ditemukan")
        continue
    print(i)

print(20*"=")

print("Continue")
for i in range(10,50,5):
    if i is number:
        print(number, "ditemukan")
        continue
    print(i)

print(20*"=")

print("Pass")
for i in range(10,50,5):
    if i is number:
        print(number, "ditemukan")
        pass
    print(i)
print(20*"=")