def parrot_trouble(talking, hour):
    if talking and hour < 7:
        return True
    if talking and hour > 20:
        return True
    return False

print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))