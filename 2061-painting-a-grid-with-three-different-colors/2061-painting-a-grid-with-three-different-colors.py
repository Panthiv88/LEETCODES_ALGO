class Solution:
    def colorTheGrid(self, m, n):
        MOD = 10**9 + 7

        def generate_patterns():
            res = []

            def backtrack(path):
                if len(path) == m:
                    res.append(tuple(path))
                    return
                for color in range(3):
                    if not path or path[-1] != color:
                        backtrack(path + [color])

            backtrack([])
            return res

        valid_rows = generate_patterns()

        transitions = {}
        for r1 in valid_rows:
            transitions[r1] = []
            for r2 in valid_rows:
                if all(a != b for a, b in zip(r1, r2)):
                    transitions[r1].append(r2)

        memo = {}

        def dp(col, prev):
            if col == n:
                return 1
            if (col, prev) in memo:
                return memo[(col, prev)]
            total = 0
            for next_row in transitions[prev]:
                total = (total + dp(col + 1, next_row)) % MOD
            memo[(col, prev)] = total
            return total

        total = 0
        for row in valid_rows:
            total = (total + dp(1, row)) % MOD
        return total
