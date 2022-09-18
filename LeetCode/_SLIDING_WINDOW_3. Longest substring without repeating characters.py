# Given a string s, find the length of the longest substring without repeating characters.

 # Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3


def lengthOfLongestSubstring(s):

    l = 0
    r = 0
    contender = 0
    longest = 0

    while r <= len(s) -1:
        for i in range(r-1, l-1, -1) :
            if s[r] == s[i]:
                l = i+1
                break
        contender = len(s[l:r+1])        
        if contender > longest:
            longest = contender
        
        r+=1
    
    return longest

s = "pwwkew"

print(lengthOfLongestSubstring(s))