class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        tgt:int = image[sr][sc]
        if tgt==color:
            return image
        queue:list[list[int]] = [[sr, sc]]
        DELTA:list[list[int]] = [[0,1],[1,0],[-1,0],[0,-1]]
        M:int=len(image)
        N:int=len(image[0])
        while queue:
            pos:list[int] = queue.pop(0)
            image[pos[0]][pos[1]]=color
            for d in DELTA:
                newpos:list[int]=[pos[0]+d[0],pos[1]+d[1]]
                if not ((0<= newpos[0] <M) and (0<= newpos[1] <N)):
                    continue
                if image[newpos[0]][newpos[1]] == tgt:
                    queue.append(newpos)
        return image