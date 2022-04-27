def max_end3(nums):
    first = nums[0]
    last = nums[-1]
    if first > last:
        return [first, first, first]
    if last > first:
        return [last, last, last]

print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))