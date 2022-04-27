def love6(a, b):
    if a == 6 or b == 6 or (a + b) == 6 or abs(a - b) == 6:
        return True
    return False

print(love6(3, 3))
print(love6(2, 6))
print(love6(1, 2))