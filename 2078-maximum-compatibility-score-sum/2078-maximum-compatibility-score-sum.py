class Solution:
    def maxCompatibilitySum(self, students, mentors):
        from itertools import permutations

        def score(s, m):
            return sum(si == mi for si, mi in zip(s, m))

        n = len(students)
        max_score = 0

        for perm in permutations(range(n)):
            total = 0
            for i in range(n):
                total += score(students[i], mentors[perm[i]])
            max_score = max(max_score, total)

        return max_score
