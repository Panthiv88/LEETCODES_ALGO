class Solution:
    def groupAnagrams(self, strs):
        from collections import defaultdict

        groups = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            groups[key].append(word)

        return list(groups.values())
