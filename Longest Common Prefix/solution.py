def letterByletter(small, big):
    newPrefix = ''
    for i in range(len(small)):
        if small[i] == big[i]:
            newPrefix += small[i]
            continue
        else: 
            break
    return newPrefix


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        
        currP = strs[0]
        
        for s in strs:
            sL = len(s)
            pL = len(currP)
            
            if (sL == 0) or (pL == 0):
                return ''
            
            elif sL >= pL:
                if currP in s[:pL]:
                    continue
                else:
                    currP = letterByletter(currP, s)
            else:
                if s in currP[:sL]:
                    currP = s
                    continue
                else:
                    currP = letterByletter(s, currP)
        return currP