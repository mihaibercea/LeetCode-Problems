def isValid(s):
    

    l = len(s)

    tries = 0   

    def check_parity(s, tries):         

        if len(s)>0:                                  
            while tries < l and len(s)>0:        
                if s[0] == "(":
                    tries = tries +1
                    for c in range(len(s)):
                        if s[c] == ")":
                            s = s[1:c:] + s[c+1:l:]
                            check_parity(s, tries)
                            break
                elif s[0] == "[":
                    tries = tries +1
                    for c in range(len(s)):
                        if s[c] == "]":
                            s = s[1:c:] + s[c+1:l:]
                            check_parity(s, tries)
                            break
                elif s[0] == "{":
                    tries = tries +1
                    for c in range(len(s)):
                        if s[c] == "}":
                            s = s[1:c:] + s[c+1:l:]
                            check_parity(s, tries)
                            break
                elif s[0] == ")" or s[0] == "]" or s[0] == "}":
                    return False
                    break

               
        if len(s)==0:
            return True
        else:
            return False
    
    return check_parity(s, tries)

print(isValid("(){}}{"))