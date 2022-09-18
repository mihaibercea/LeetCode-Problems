# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def containsDuplicate(nums):
    result = False
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            result= True            
    return result
nums1 = [2,14,18,22,22]

print(containsDuplicate(nums1))