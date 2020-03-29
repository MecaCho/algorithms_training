"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.ret = 0
        hash_map = dict()
        for employee in employees:
            hash_map[employee.id] = [employee.importance, employee.subordinates]

        def dfs(id):
            if hash_map.get(id):
                self.ret += hash_map[id][0]
                for id in hash_map[id][1]:
                    dfs(id)

        dfs(id)

        return self.ret

