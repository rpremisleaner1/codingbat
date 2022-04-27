def front_back(str):
    first = str[0]
    last = str[-1]
    other = str[1:-1]
    return last + other + first

print(front_back('code'))