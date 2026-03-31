class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''

        for c in s:
            if c.isalnum():
                newStr += c.lower()

        last = len(newStr) - 1
        for i in range(len(newStr)):
            if not newStr[i] == newStr[last - i]:
                return False
        return True