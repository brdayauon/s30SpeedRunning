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

"""
MY SOLUTION EZPZ FROM THE DOME
"""
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
            hm[employee.id] = employee
        total = 0
        stack = [id]
        while stack:
            e = stack.pop() 
            if e in hm:
                total += hm[e].importance
                employees = hm[e].subordinates
                for person in employees:
                    stack.append(person)
        return total

"""
ANOTHER SOLUTION FROM THE DOME
"""
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
        total = 0
        stack = [id]
        for employee in employees:
            hm[employee.id] = employee
        
        while stack:
            person = stack.pop()
            employee = hm[person]
            total += employee.importance 
            for neighbors in (employee.subordinates):
                stack.append(neighbors)
                
        return total