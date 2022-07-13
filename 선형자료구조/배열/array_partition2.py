def arrayPairSum(nums: list) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum


print(arrayPairSum([1, 4, 3, 2]))
