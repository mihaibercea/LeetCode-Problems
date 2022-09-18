# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):
    longest = s[0]
    if len(s) == 0:
        return 0
    else:
        contender = s[0]



    for char in s[1:]:
        for i in range(len(contender)):
            if char == contender[i]:
                contender = contender[i+1:]
                break
        contender = contender + char        
        if len(contender) > len(longest):
            longest = contender

    return len(longest)

s = ' '
print(lengthOfLongestSubstring(s))