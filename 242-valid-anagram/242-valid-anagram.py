class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        al:list[int] = [0]*26
        for c in s:
            al[ord(c)-ord('a')]+=1
        for c in t:
            al[ord(c)-ord('a')]-=1
            if al[ord(c)-ord('a')]<0:
                return False
        for i in al:
            if i!=0:
                return False
        return True