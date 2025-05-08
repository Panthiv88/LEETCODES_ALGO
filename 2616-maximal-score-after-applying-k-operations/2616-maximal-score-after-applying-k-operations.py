import heapq

class Solution:
    def maxKelements(self, nums, k):
        nums = [-x for x in nums]
        heapq.heapify(nums)
        score = 0
        for _ in range(k):
            top = -heapq.heappop(nums)
            score += top
            heapq.heappush(nums, -((top + 2) // 3))
        return score
