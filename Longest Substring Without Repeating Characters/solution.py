class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0

        temp = ''

        for i in s:
            if i in temp:
                size = len(temp)
                if size > counter:
                    counter = size
                
                x = temp.index(i)
                temp = temp[x+1:]
                temp += i
            else:
                temp += i

        if temp != '':
            if len(temp) > counter:
                counter = len(temp)
    
        return counter
