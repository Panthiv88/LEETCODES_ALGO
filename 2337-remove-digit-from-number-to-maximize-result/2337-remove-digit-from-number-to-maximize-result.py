class Solution:
    def removeDigit(self, number, digit):
        result = []
        for i in range(len(number)):
            if number[i] == digit:
                result.append(number[:i] + number[i+1:])
        return max(result)
