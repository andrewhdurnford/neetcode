class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for c in s:
            if c.isalnum():
                new += c.lower()
        last = len(new) - 1
        for i in range(len(new)):
            if not new[i] == new[last - i]:
                return False
        return True