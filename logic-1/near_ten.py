def near_ten(num):
    return 0 <= (num % 10) <= 2 or 8 <= (num % 10) <= 10

print(near_ten(12))
print(near_ten(10))
print(near_ten(17))