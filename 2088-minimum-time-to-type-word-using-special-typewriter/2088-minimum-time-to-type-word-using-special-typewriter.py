class Solution:
    def minTimeToType(self, word):
        time = 0
        current = 'a'

        for c in word:
            diff = abs(ord(c) - ord(current))
            step = min(diff, 26 - diff)
            time += step + 1  # +1 for typing the character
            current = c

        return time
