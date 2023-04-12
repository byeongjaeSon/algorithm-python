class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, acc):
            if root is None: return 0
            if root.left is None and root.right is None: return acc * 10 + root.val
            return dfs(root.left, acc * 10 + root.val) + dfs(root.right, acc * 10 + root.val)
            
        return dfs(root, 0)