def front3(str):
    if len(str) < 3:
        return str * 3
    return str[0:3] * 3

print(front3('abc'))
print(front3('Chocolate'))