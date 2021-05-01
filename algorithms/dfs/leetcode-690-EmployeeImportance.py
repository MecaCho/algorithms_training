# encoding=utf8


'''
690. Employee Importance

You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
 

Note:

One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.


690. 员工的重要性

给定一个保存员工信息的数据结构，它包含了员工 唯一的 id ，重要度 和 直系下属的 id 。

比如，员工 1 是员工 2 的领导，员工 2 是员工 3 的领导。他们相应的重要度为 15 , 10 , 5 。那么员工 1 的数据结构是 [1, 15, [2]] ，员工 2的 数据结构是 [2, 10, [3]] ，员工 3 的数据结构是 [3, 5, []] 。注意虽然员工 3 也是员工 1 的一个下属，但是由于 并不是直系 下属，因此没有体现在员工 1 的数据结构中。

现在输入一个公司的所有员工信息，以及单个员工 id ，返回这个员工和他所有下属的重要度之和。

 

示例：

输入：[[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
输出：11
解释：
员工 1 自身的重要度是 5 ，他有两个直系下属 2 和 3 ，而且 2 和 3 的重要度均为 3 。因此员工 1 的总重要度是 5 + 3 + 3 = 11 。
 

提示：

一个员工最多有一个 直系 领导，但是可以有多个 直系 下属
员工数量不超过 2000 。
'''



"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        importances = dict()
        sub_dict = dict()
        
        for e in employees:
            importances[e.id] = e.importance
            sub_dict[e.id] = e.subordinates
        
        def dfs(id):
            return importances[id] + sum([dfs(sub) for sub in sub_dict[id]])

        return dfs(id)

# golang solution

'''
/**
 * Definition for Employee.
 * type Employee struct {
 *     Id int
 *     Importance int
 *     Subordinates []int
 * }
 */

func getImportance(employees []*Employee, id int) int {

    employeesDict := make(map[int]*Employee, len(employees))

    for _, employee := range employees{
		employeesDict[employee.Id] = employee
	}

	var dfs func(int) int
	dfs = func(id int) int {
		res := employeesDict[id].Importance
		for _, id_ := range employeesDict[id].Subordinates {
			res += dfs(id_)
		}
		return res
	}

	return dfs(id)
    
}
'''


# solutions

'''
前言
由于一个员工最多有一个直系领导，可以有零个或若干个直系下属，因此员工之间的领导和下属关系构成树的结构。给定一个员工编号，要求计算这个员工及其所有下属的重要性之和，即为找到以该员工为根节点的子树的结构中，每个员工的重要性之和。

对于树结构的问题，可以使用深度优先搜索或广度优先搜索的方法解决。

方法一：深度优先搜索
深度优先搜索的做法非常直观。根据给定的员工编号找到员工，从该员工开始遍历，对于每个员工，将其重要性加到总和中，然后对该员工的每个直系下属继续遍历，直到所有下属遍历完毕，此时的总和即为给定的员工及其所有下属的重要性之和。

实现方面，由于给定的是员工编号，且每个员工的编号都不相同，因此可以使用哈希表存储每个员工编号和对应的员工，即可通过员工编号得到对应的员工。

JavaC#JavaScriptGolangC++Python3

func getImportance(employees []*Employee, id int) (total int) {
    mp := map[int]*Employee{}
    for _, employee := range employees {
        mp[employee.Id] = employee
    }

    var dfs func(int)
    dfs = func(id int) {
        employee := mp[id]
        total += employee.Importance
        for _, subId := range employee.Subordinates {
            dfs(subId)
        }
    }
    dfs(id)
    return
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是员工数量。需要遍历所有员工，在哈希表中存储员工编号和员工的对应关系，深度优先搜索对每个员工遍历一次。

空间复杂度：O(n)O(n)，其中 nn 是员工数量。空间复杂度主要取决于哈希表的空间和递归调用栈的空间，哈希表的大小为 nn，栈的深度不超过 nn。

方法二：广度优先搜索
也可以使用广度优先搜索的做法。

和深度优先搜索一样，使用哈希表存储每个员工编号和对应的员工，即可通过员工编号得到对应的员工。根据给定的员工编号找到员工，从该员工开始广度优先搜索，对于每个遍历到的员工，将其重要性加到总和中，最终得到的总和即为给定的员工及其所有下属的重要性之和。

JavaC#JavaScriptGolangC++Python3

func getImportance(employees []*Employee, id int) (total int) {
    mp := map[int]*Employee{}
    for _, employee := range employees {
        mp[employee.Id] = employee
    }

    queue := []int{id}
    for len(queue) > 0 {
        employee := mp[queue[0]]
        queue = queue[1:]
        total += employee.Importance
        for _, subId := range employee.Subordinates {
            queue = append(queue, subId)
        }
    }
    return
}
复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是员工数量。需要遍历所有员工，在哈希表中存储员工编号和员工的对应关系，广度优先搜索对每个员工遍历一次。

空间复杂度：O(n)O(n)，其中 nn 是员工数量。空间复杂度主要取决于哈希表的空间和队列的空间，哈希表的大小为 nn，队列的大小不超过 nn。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/employee-importance/solution/yuan-gong-de-zhong-yao-xing-by-leetcode-h6xre/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''


