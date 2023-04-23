class Solution:
    def isPalindrome(self, s: str) -> bool:
        vs:str = ''.join(filter(str.isalnum, s)).lower()
        return vs[::-1]==vs