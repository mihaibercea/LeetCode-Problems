

from tkinter import S


def isPalindrome(s):
        
    s = ''.join(filter(str.isalnum, s))
    s = s.lower()
    
    back = len(s)//2
    forth = len(s)//2 + len(s)%2 + 1
    
    while back > 0:
        
        if s[back-1] != s[forth-1]:
            return False
        
        back-=1
        forth+=1
    
    return True

s1 = "A man, a plan, a canal: Panama"
print(isPalindrome(s1))

        