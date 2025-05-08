class Solution:
    def postorderTraversal(self, root):
        result = []
        stack = []
        last_visited = None
        current = root

        while current or stack:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek = stack[-1]
                if peek.right and last_visited != peek.right:
                    current = peek.right
                else:
                    result.append(peek.val)
                    last_visited = stack.pop()

        return result
