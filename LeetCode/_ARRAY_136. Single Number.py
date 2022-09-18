# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

from argparse import ONE_OR_MORE


def singleNumber(nums):
    nums_check = []    
    for num in nums:
        if len(nums_check) == 0:
            nums_check.append(num)
        elif num == nums_check[0]:
            nums_check.pop([0])
        elif num==nums_check[len(nums_check)]:
            nums_check.pop()
        elif num != nums_check[0]:
            nums_check.append(num)

    return nums_check[0]

def singleNumber_nonlinear(nums):
    nums_check = []
    for num in nums:
        if len(nums_check) == 0:
            nums_check.append(num)
        elif num in nums_check:
            nums_check.remove(num)
        else:
            nums_check.append(num)
    return nums_check[0]
    
nums = [1, 2, 2, 1, 3, 4, 5, 3, 4]

def singleNumber_leetcode_boss(self, nums: List[int]) -> int:
	return reduce(lambda total, el: total ^ el, nums)

print(singleNumber_nonlinear(nums))

