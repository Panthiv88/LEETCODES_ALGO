class Solution:
    def topStudents(self, positive_feedback, negative_feedback, report, student_id, k):
        pos = set(positive_feedback)
        neg = set(negative_feedback)
        scores = []

        for i in range(len(report)):
            words = report[i].split()
            score = 0
            for word in words:
                if word in pos:
                    score += 3
                elif word in neg:
                    score -= 1
            scores.append(( -score, student_id[i]))  # Negative score for sorting

        scores.sort()
        return [sid for _, sid in scores[:k]]
