# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.

             

def characterReplacement(s, k):
    
    count = {}

    l = 0
    r = 0 

    contender = 0
    longest = 1

    for r in range(len(s)):
        
        if s[r] not in count.keys():
            count[s[r]] = 1

        else:
            count[s[r]]+=1
        
        maxim = max(maxim, count[s[r]])

        substr = s[l:r+1]

        x = len(substr)

        if len(s[l:r+1]) - maxim > k:

            count[s[l]]-=1
            l = l+1
            

        else:
            contender = len(s[l:r+1])
        
            if contender > longest:
                longest = contender
        
            
    return longest

s1 = "ABAA"
k1 = 0

print(characterReplacement(s1, k1))

#print(len(set(s1[0:4])))

# print(len(set("AABA")))
# print(len(set("AAB")))

