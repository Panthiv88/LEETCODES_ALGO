class Solution:
    def grayCode(self, n):
        result = [0]
        for i in range(n):
            add = 1 << i
            for j in reversed(range(len(result))):
                result.append(result[j] + add)
        return result
