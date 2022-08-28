# encoding=utf8

'''
793. Preimage Size of Factorial Zeroes Function
Let f(x) be the number of zeroes at the end of x!. Recall that x! = 1 * 2 * 3 * ... * x and by convention, 0! = 1.

For example, f(3) = 0 because 3! = 6 has no zeroes at the end, while f(11) = 2 because 11! = 39916800 has two zeroes at the end.
Given an integer k, return the number of non-negative integers x have the property that f(x) = k.

 

Example 1:

Input: k = 0
Output: 5
Explanation: 0!, 1!, 2!, 3!, and 4! end with k = 0 zeroes.
Example 2:

Input: k = 5
Output: 0
Explanation: There is no x such that x! ends in k = 5 zeroes.
Example 3:

Input: k = 3
Output: 5
 

Constraints:

0 <= k <= 109
'''

# golang

'''
func preimageSizeFZF(k int) int {
    return nx(k+1) - nx(k)
}

func zeta(n int) (res int) {
    for n > 0 {
        n /= 5
        res += n
    }
    return
}

func nx(k int) int {
    return sort.Search(5*k, func(x int) bool { return zeta(x) >= k })
}
'''

