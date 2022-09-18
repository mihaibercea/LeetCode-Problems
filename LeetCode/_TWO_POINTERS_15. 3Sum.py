
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):

    res = []

    if len(nums) == 3:
        
        if nums[0] + nums[1] + nums[2] == 0:
            
            res.append(nums)

    else:
        nums = sorted(nums)

        p1_set = set()
        # p2_set = set()
        
        for p1 in range(len(nums)-2):

            if nums[p1] not in p1_set:

                p1_set.add(nums[p1])

                front = p1+1
                back = len(nums) - 1

                while (back > front):

                    # p2_set.add(nums[front])

                    if nums[front]+nums[back] == 0 - nums[p1]:

                        res.append([nums[p1], nums[front], nums[back]])
                        
                        while nums[front]==nums[front+1] and front < back-1:
                            front +=1
                        
                        front +=1

                    elif nums[front]+nums[back] > 0 - nums[p1]:

                        back -=1
                    
                    elif nums[front]+nums[back] < 0 - nums[p1]:
                        
                        front +=1

                                    
              
        
    return res

nums1 = [-1,0,1,2,-1,-4]
nums2 = [0,0,0,0]
print(threeSum(nums2))


