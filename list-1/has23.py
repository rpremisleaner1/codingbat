def has23(nums):
    if 2 in nums or 3 in nums:
        return True
    return False

print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))