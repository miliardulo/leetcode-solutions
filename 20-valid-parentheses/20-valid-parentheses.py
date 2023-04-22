class Solution:
    def isValid(self, s: str) -> bool:
        stk:list[str] = list()
        left:tuple[str] = ("(","{","[")
        right:tuple[str] = (')','}',']')
        for c in s:
            if c in left:
                stk.append(c)
                continue
            if len(stk)==0:
                return False
            if stk[-1]==left[right.index(c)]:
                stk.pop()
                continue
            return False
        return not stk
            