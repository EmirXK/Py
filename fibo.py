a = 0
b = 1
temp = 0
print(a)
print(b)

while True:
    c = a+b
    if c > 999999:
        break
    print(str(a) + " + " + str(b) + " = " + str(c))
    temp = b
    b = c
    a = temp
