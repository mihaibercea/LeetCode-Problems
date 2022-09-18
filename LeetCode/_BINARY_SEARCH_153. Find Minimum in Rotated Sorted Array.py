# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time
    
def search(nums):

    if len(nums) == 1:
        return len[0]
    
    l = 0
    r = len(nums)-1
    half = ((r+l)//2)

    while l<r:
        if r == l+1:
            return min(nums[l], nums[r])
        elif nums[half]>nums[r]:
            l = half
            half = ((r+l)//2)
        elif nums[half]<nums[r]:
            if nums[l]<nums[half]:
                return nums[l]
            else:
                r = half
                half = ((r+l)//2)
    


nums = [1,2,3]
target = 0

print(search(nums ))