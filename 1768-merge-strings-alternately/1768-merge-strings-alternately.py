class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1: int = len(word1)
        l2: int = len(word2)
        i1: int = 0
        i2: int = 0
        mstr: str = ''
        while i1<l1 and i2<l2:
            mstr+=word1[i1]
            i1+=1
            mstr+=word2[i2]
            i2+=1
        mstr+=word1[i1:]
        mstr+=word2[i2:]
        return mstr
            