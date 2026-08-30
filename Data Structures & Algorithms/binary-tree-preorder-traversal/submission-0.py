# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        q = []
        vals = []
        q.append(root)
        while q :
            curr = q.pop()
            st = []
            while curr :
                vals.append(curr.val)
                if curr.right :
                    st.append(curr.right)
                curr = curr.left
            q = q + st

        return vals
