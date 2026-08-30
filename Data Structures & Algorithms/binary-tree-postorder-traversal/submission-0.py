# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        if root :
            st = []
            seen = set()
            st.append(root)
            while st :
                curr = st.pop()
                smst = []
                while curr and curr not in seen:
                    smst.append(curr)
                    if curr.right and curr.right not in seen:
                        smst.append(curr.right)
                    if curr.left and curr.left not in seen:
                        smst.append(curr.left)
                    seen.add(curr)
                    curr = smst.pop()
                vals.append(curr.val)
                st = st + smst
        return vals
            
                