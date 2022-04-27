def left2(str):
    last = str[0:2]
    first = str[2:]
    return first + last

print(left2('Hello'))
print(left2('java'))