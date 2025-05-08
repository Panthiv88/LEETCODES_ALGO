class Solution:
    def minMovesToSeat(self, seats, students):
        seats.sort()
        students.sort()
        return sum(abs(s - t) for s, t in zip(seats, students))
