from typing import List

def twoSum(nums: List[int], target:int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums:
            return [nums.index(n), nums.index(complement)]

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))