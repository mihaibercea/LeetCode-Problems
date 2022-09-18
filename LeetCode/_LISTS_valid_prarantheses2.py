def isValid(s):

    s_list = list(s)
   
    def check_parity(s):
        copy_s = []
        for a in s_list:
            copy_s.append(0)
        print(copy_s)
        count = 0
        while count < len(s):
            for x in range(len(s_list)):
                count = count +1
                if s_list[x] == "(":
                    for y in range(x, len(s_list)):
                        if s_list[y] == ")":
                            copy_s[x] = s_list[x]
                            copy_s[y] = s_list[y]                 
                            break
                if s_list[x] == "[":
                    for y in range(x, len(s_list)):
                        if s_list[y] == "]":
                            copy_s[x] = s_list[x]
                            copy_s[y] = s_list[y]                      
                            break
                if s_list[x] == "{":
                    for y in range(x, len(s_list)):
                        if s_list[y] == "}":
                            copy_s[x] = s_list[x]
                            copy_s[y] = s_list[y]                         
                            break

        if  len(copy_s) == len(s_list) :
            return True
        else:
            return False
    
    return check_parity(s)

print(isValid("({{{{}}}))"))