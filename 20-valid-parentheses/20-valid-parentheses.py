class Solution:
    def isValid(self, s: str) -> bool:
        stk:list[str] = list()
        pair:dict[str,str] = {'(':')','[':']','{':'}'}
        for c in s:
            if c in pair.keys():
                stk.append(c)
                continue
            if len(stk)==0 or c!=pair[stk[-1]]:
                return False
            stk.pop()
        return not stk
        
            