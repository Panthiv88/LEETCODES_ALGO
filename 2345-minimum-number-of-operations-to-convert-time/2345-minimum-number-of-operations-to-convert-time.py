class Solution:
    def convertTime(self, current, correct):
        h1, m1 = map(int, current.split(":"))
        h2, m2 = map(int, correct.split(":"))
        total_minutes = (h2 * 60 + m2) - (h1 * 60 + m1)
        ops = 0
        for step in [60, 15, 5, 1]:
            ops += total_minutes // step
            total_minutes %= step
        return ops
