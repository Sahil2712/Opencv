c1 = 1

def dothis():
    global count
    for i in (1, 2, 3):
        c1 += 1
dothis()
print(c1)