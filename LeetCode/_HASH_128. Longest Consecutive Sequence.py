# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


def longestConsecutive(nums) -> bool:

    contender = []
    longest = []
    nums_set = set(nums)

    nums_set_list = list(nums_set)

    some sort of recursion

    for num in nums_set_list:
        contender.append[num]
        nums_set_list.remove(num)
        before = contender[0] - 1
        after = contender[0] - 1
        if before in nums_set:
            contender.insert(0, before)
            nums_set_list.remove(before)
        if after in nums_set:
            contender.insert(len(contender), after)
            nums_set_list.remove(before) 
        
    return len(longest)
    
nums = [100,4,200,1,3,2]
nums1 = [0,3,7,2,5,8,4,6,0,1]

print(longestConsecutive(nums))

