#A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

#The path sum of a path is the sum of the node's values in the path.
#Given the root of a binary tree, return the maximum path sum of any path.

 

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def solve(root,ans):
            if root==None:
                return 0
            l=solve(root.left,ans)
            r=solve(root.right,ans)
            temp=max(max(l,r)+root.val,root.val)
            res=max(l+r+root.val,temp)
            ans[0]=max(ans[0],res)
            return temp
        ans=[-inf]
        solve(root,ans)
        return ans[0]