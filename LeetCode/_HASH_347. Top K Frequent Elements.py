# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

def topKFrequent(nums, k):
    res = []
    nums_set = set(nums)
    nums_dict = dict.fromkeys(nums_set, 0)

    for num in nums:
        nums_dict[num] += 1
    
    test = sorted(nums_dict.items(), key=lambda item: item[1])

    nums_dict = dict(test)

    res = list(nums_dict.values())
    res = res[:k]
    return res

nums1 = [1,1,1,2,2,3, 4, 4, 4, 5, 6, 6, 6, 6]

print(topKFrequent(nums1, 2))