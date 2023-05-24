# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findx(self, root: 'TreeNode', x: int, que: list[TreeNode])->list[TreeNode]:
        que.append(root)
        if root.val == x:
            return que
        if root.val < x:
            return self.findx(root.right,x,que)
        return self.findx(root.left,x,que)
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        quep:list[TreeNode] = self.findx(root,p.val,[])
        queq:list[TreeNode] = self.findx(root,q.val,[])
        if len(quep)>len(queq):
            quep,queq = queq,quep
        idx:int = len(quep)-1
        while quep[idx]!=queq[idx]:
            idx-=1
        return quep[idx]