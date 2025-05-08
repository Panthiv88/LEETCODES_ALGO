class Solution:
    def isHappy(self, n):
        def get_sum_of_squares(num):
            return sum(int(x) ** 2 for x in str(num))

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_sum_of_squares(n)

        return n == 1
