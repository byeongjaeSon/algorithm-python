class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []

        if not root:
            return preorder
        
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                preorder.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return preorder
