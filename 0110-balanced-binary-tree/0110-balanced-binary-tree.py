class Solution:
    def isBalanced(self, root):
        def check(node):
            if not node:
                return 0, True

            left_height, left_balanced = check(node.left)
            right_height, right_balanced = check(node.right)

            height = 1 + max(left_height, right_height)
            balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            return height, balanced

        return check(root)[1]
