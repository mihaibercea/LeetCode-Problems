# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

import math


def productExceptSelf(nums):
    res = [1] * len(nums)

    prefix = 1

    for i in range(len(nums)):

        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums)-1, -1, -1):

        res[i] = postfix*res[i]
        postfix *= nums[i]

    return res

nums1 = [1, 2, 3, 4, 5]

print(productExceptSelf(nums1))