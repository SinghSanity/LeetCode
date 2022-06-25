# String Comprehension Solution
class Solution_A:
    def isPalindrome(self, x: int) -> bool:

        s = str(x)
        if s == s[::-1]:
            return True

        return False


# Non-String Comprehension Solution
class Solution_B:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False

        temp = x
        rev = 0
        while (x > 0):
            dig=x%10
            rev = rev * 10 + dig
            x = x // 10
        if (temp == rev):
            return True

        return False
