class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = 0
        right = 0
        for i in range(len(weights)):
            left = max(left, weights[i])
            right += weights[i]
            
        while left <= right:
            middle = left + (right-left)//2
            count = 0
            tempDays = 0
            for i in range(len(weights)):
                count += weights[i]
                if count > middle:
                    tempDays += 1
                    count = weights[i]
            if tempDays >= days:
                left = middle+1
            else:
                right = middle-1
        return left
                