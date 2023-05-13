class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False

            if left.val == right.val:
                outPair = isMirror(left.left, right.right)
                inPiar = isMirror(left.right, right.left)
                return outPair and inPiar
            else:
                return False

        return isMirror(root.left, root.right)