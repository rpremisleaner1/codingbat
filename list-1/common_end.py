def common_end(a, b):
    if a[0] == b[0]:
        return True
    if a[-1] == b[-1]:
        return True
    else:
        return False

print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))