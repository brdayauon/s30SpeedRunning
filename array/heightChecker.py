"""
make another array thats sorted... iterate through both at the same time
if not the same increase count.

get frequency arr... 
decrease each count by one when we reach the height.. if prev height isn't it
increase count by 1
"""
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        total = 0
        
        for i in range(len(heights)):
            if heights[i] != sortedHeights[i]:
                total += 1
        return total


"""
make another array thats sorted... iterate through both at the same time
if not the same increase count.

get frequency arr... 
decrease each count by one when we reach the height.. if prev height isn't it
increase count by 1
"""
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        mx = max(heights)
        countArr = [0 for i in range(mx+1)]
        
        for i in range(len(heights)):
            countArr[heights[i]] += 1
        
        currentHeight = 0 
        res = 0
        for i in range(len(heights)):
            while countArr[currentHeight] == 0:
                currentHeight += 1
            if heights[i] != currentHeight:
                res += 1
            countArr[currentHeight] -= 1
        return res