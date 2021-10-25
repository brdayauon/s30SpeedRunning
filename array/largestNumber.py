class Comparable:
    def __init__(self, num):
        self.val = str(num)
        
    def __lt__(self, other):
        return self.val+other.val  > other.val + self.val 
    def __gt__(self, other):
        return self.val+other.val < other.val + self.val 
    def __eq__(self, other):
        return self.val + other.val == other.val + self.val 
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #create array to hold the compared values
        sortedNums = []
        
        #put number from nums to sortedNums[] comparable value 
        for num in nums:
            sortedNums.append(Comparable(num))
        sortedNums = sorted(sortedNums)
        
        res = []
        for num in sortedNums:
            res.append(num.val)
        
        stringRes = ''.join(res)
        if stringRes[0] == '0':
            return '0'
        return ''.join(res)