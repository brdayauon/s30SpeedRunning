"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        hm = {}
        
        for employee in employees:
            if employee.id not in hm:
                hm[employee.id] = []
            hm[employee.id] = employee
        
        total = 0        
        stack = []
        stack.append(id)
        
        while stack:
            employeeId = stack.pop()
            employee = hm[employeeId]
            total += employee.importance 
            
            for sub in employee.subordinates:
                stack.append(sub)
                
        return total