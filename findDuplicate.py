class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        
        while True: #while fast and fast.next 
            slow = nums[slow] #slow=slow.next
            fast = nums[nums[fast]] #fast = fast.next.next
            if slow == fast:
                break
                
        #reset pointers
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast