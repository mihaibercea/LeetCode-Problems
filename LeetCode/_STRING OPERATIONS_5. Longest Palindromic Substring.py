# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.


from tkinter import S


def longestPalindrome(s):

    

    if len(s) == 0:
        return ''
    
    elif len(s) == 1:
        return s
        
    else:
        substring = s[0]
        longest = s[0]
        contender = ''
        uniques = numberOfUniques(S)

        for i in range(len(s)):
            j = 0
            while (len(s)-j)>=i:                
                substring = s[i:len(s)-j]

                if len(longest) > len(substring):
                    break

                elif isPalindrome(substring):
                    contender = substring

                if len(contender) > len(longest):
                    longest = contender

                if len(longest) == (2*uniques -1):
                    break

                j+=1
                    
        return longest
            
def numberOfUniques(s):
    reduced = ''
    for char in s:
        if char not in reduced:
            reduced += char
    
    return len(reduced)

def isPalindrome(s):    
    
    if len(s) == 0 or len(s) == 1:
        return True
    elif s[0] == s[len(s)-1]:
        s = s[1:len(s)-1]
        return isPalindrome(s)
    else:
        return False

s1 = 'aba'
s2 = 'abccba'

s3 = 'cbbd'

print(isPalindrome(s1))
print(isPalindrome(s2))
print(longestPalindrome(s3))

print(numberOfUniques(s2))
    
