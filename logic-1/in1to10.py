def in1to10(n, outside_mode):
    if outside_mode is False:
        return n in range (1, 11)
    return n <= 1 or n >= 10

print(in1to10(2, False))