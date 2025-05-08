class Solution:
    def minimumSum(self, num):
        digits = sorted([int(d) for d in str(num)])
        return digits[0]*10 + digits[2] + digits[1]*10 + digits[3]
