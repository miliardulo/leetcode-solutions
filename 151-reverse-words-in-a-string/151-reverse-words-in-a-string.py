class Solution:
    def reverseWords(self, s: str) -> str:
        wl: List[str] = list(filter(lambda x: x, s.split(' ')))[::-1]
        return ' '.join(wl)