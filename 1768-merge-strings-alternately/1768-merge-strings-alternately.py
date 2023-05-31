class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1: int = len(word1)
        l2: int = len(word2)
        i1: int = 0
        i2: int = 0
        slst: List[str] = []
        while i1<l1 and i2<l2:
            slst.append(word1[i1])
            i1+=1
            slst.append(word2[i2])
            i2+=1
        slst.append(word1[i1:])
        slst.append(word2[i2:])
        return ''.join(slst)
            