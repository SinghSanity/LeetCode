def convertToString(num):
    string = ''
    if num >= 0:
        string = str(num)
        string = string[::-1]
    else:
        string = str(abs(num))
        string = "-" + string[::-1]
    
    return string    


def intCompare(string):
    isNegative = False
    s = string
    if "-" in string:
        isNegative = True
        s = s.strip("-")
        
    sLen = len(s)
    
    if sLen > 10:
        return 0
    
    elif sLen < 10:
        return result(isNegative, s)
        
    else:
        # limit for postive ints is 2147483647
        limit1 = '214748364'
        
        if isNegative:
            limit2 = '8'
        else:
            limit2 = '7'
            
        s1 = s[:-1]
        s2 = s[-1]
        
        if int(s1) > int(limit1):
            return 0
        
        elif int(s1) < int(limit1):
            return result(isNegative, s)
            
        else:
            if int(s2) > int(limit2):
                return 0
            else:
                return result(isNegative, s)
                
def result(status, string):
    if status:
        string = '-' + string
    return int(string)
    
    
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else:
            s = convertToString(x)
            return intCompare(s)         
