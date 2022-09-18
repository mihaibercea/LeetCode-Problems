# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.
       

def checkInclusion(s1, s2):
    
    l=0
    r=len(s1)-1

    counts1 = {}

    for c in s1:
        if c in counts1.keys():
            counts1[c]+=1
        else:
            counts1[c]=1
    
    count = {}

    for c in s2[0:r]:
        if c in count.keys():
            count[c]+=1
        else:
            count[c]=1

    while r < len(s2):

        if s2[r] in count.keys():
                count[s2[r]]+=1
        else:
            count[s2[r]]=1

        test = s2[l:r+1]

        if count == counts1:
            return True     
        
        else:
            count[s2[l]]-=1

            if count[s2[l]] == 0:
                del count[s2[l]]
            l+=1
            r+=1            
    
    return False

s1 = "ab"
s2 = "eidbaooo"

print(checkInclusion(s1, s2))