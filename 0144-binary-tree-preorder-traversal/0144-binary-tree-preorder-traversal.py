class Solution:
    def preorderTraversal(self, root):
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                result.append(current.val)
                stack.append(current)
                current = current.left
            current = stack.pop()
            current = current.right

        return result
