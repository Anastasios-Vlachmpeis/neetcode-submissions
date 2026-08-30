# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        def req(arr, node) -> None:
            if not node :
                return
            req(arr, node.left)
            arr.append(node.val)
            req(arr, node.right)
        
        arr = []

        req(arr, root)

        return arr
                