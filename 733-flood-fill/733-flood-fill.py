class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        M:int=len(image)
        N:int=len(image[0])
        visited:list[list[bool]]=[[False for _ in range(N)] for _ in range(M)]
        queue:list[list[int]] = [[sr, sc]]
        tgt:int = image[sr][sc]
        DELTA:list[list[int]] = [[0,1],[1,0],[-1,0],[0,-1]]
        while queue:
            pos:list[int] = queue.pop(0)
            image[pos[0]][pos[1]]=color
            visited[pos[0]][pos[1]]=True
            for d in DELTA:
                newpos:list[int]=[pos[0]+d[0],pos[1]+d[1]]
                if not ((0<= newpos[0] <M) and (0<= newpos[1] <N)):
                    continue
                if image[newpos[0]][newpos[1]] == tgt and not visited[newpos[0]][newpos[1]]:
                    queue.append(newpos)
        return image