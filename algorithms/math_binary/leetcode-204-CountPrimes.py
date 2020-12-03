'''
204. Count Primes
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

204. 计数质数
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
'''


import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        is_prime_dict = [1] * n
        is_prime_dict[:2] = [0 ] *2
        def is_prime(num):
            for i in range(2, int(math.sqrt(num) ) +1):
                if num % i == 0:
                    return False
            return True


        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime(i):
                is_prime_dict[ i *2:n:i] = [0] * (( n -1 - 2* i) // i + 1)

        return sum(is_prime_dict)



class Solution20201203(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        def is_prime(n):
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return False
            return True
        if n < 2:
            return 0
        prime_dict = [1 for _ in range(n)]

        for i in range(2, int(math.sqrt(n))+1):
            if is_prime(i):
                prime_dict[i*2:n:i] = [0]*((n-1 - i*2)//i+1)

        return sum(prime_dict) - 2


if __name__ == '__main__':
    print(bin(100)[::-1][:-2])

#  solution

'''
前言
统计 [2,n][2,n] 中质数的数量是一个很常见的题目，也有很多巧妙高效的做法，接下来的部分只会讲述一些常见的做法，更多的拓展内容读者可以自行搜索补充，也欢迎在评论区与大家分享交流。

方法一：枚举
很直观的思路是我们枚举每个数判断其是不是质数。

考虑质数的定义：在大于 11 的自然数中，除了 11 和它本身以外不再有其他因数的自然数。因此对于每个数 xx，我们可以从小到大枚举 [2,x-1][2,x−1] 中的每个数 yy，判断 yy 是否为 xx 的因数。但这样判断一个数是否为质数的时间复杂度最差情况下会到 O(n)O(n)，无法通过所有测试数据。

考虑到如果 yy 是 xx 的因数，那么 \frac{x}{y} 
y
x
​	
  也必然是 xx 的因数，因此我们只要校验 yy 或者 \frac{x}{y} 
y
x
​	
  即可。而如果我们每次选择校验两者中的较小数，则不难发现较小数一定落在 [2,\sqrt{x}][2, 
x
​	
 ] 的区间中，因此我们只需要枚举 [2,\sqrt{x}][2, 
x
​	
 ] 中的所有数即可，这样单次检查的时间复杂度从 O(n)O(n) 降低至了 O(\sqrt{n})O( 
n
​	
 )。

C++JavaJavaScriptGolangC

// 超时警告
func isPrime(x int) bool {
    for i := 2; i*i <= x; i++ {
        if x%i == 0 {
            return false
        }
    }
    return true
}

func countPrimes(n int) (cnt int) {
    for i := 2; i < n; i++ {
        if isPrime(i) {
            cnt++
        }
    }
    return
}
复杂度分析

时间复杂度：O(n\sqrt{n})O(n 
n
​	
 )。单个数检查的时间复杂度为 O(\sqrt{n})O( 
n
​	
 )，一共要检查 O(n)O(n) 个数，因此总时间复杂度为 O(n\sqrt{n})O(n 
n
​	
 )。

空间复杂度：O(1)O(1)。

方法二：埃氏筛
枚举没有考虑到数与数的关联性，因此难以再继续优化时间复杂度。接下来我们介绍一个常见的算法，该算法由希腊数学家厄拉多塞（\rm EratosthenesEratosthenes）提出，称为厄拉多塞筛法，简称埃氏筛。

我们考虑这样一个事实：如果 xx 是质数，那么大于 xx 的 xx 的倍数 2x,3x,\ldots2x,3x,… 一定不是质数，因此我们可以从这里入手。

我们设 \textit{isPrime}[i]isPrime[i] 表示数 ii 是不是质数，如果是质数则为 11，否则为 00。从小到大遍历每个数，如果这个数为质数，则将其所有的倍数都标记为合数（除了该质数本身），即 00，这样在运行结束的时候我们即能知道质数的个数。

这种方法的正确性是比较显然的：这种方法显然不会将质数标记成合数；另一方面，当从小到大遍历到数 xx 时，倘若它是合数，则它一定是某个小于 xx 的质数 yy 的整数倍，故根据此方法的步骤，我们在遍历到 yy 时，就一定会在此时将 xx 标记为 \textit{isPrime}[x]=0isPrime[x]=0。因此，这种方法也不会将合数标记为质数。

当然这里还可以继续优化，对于一个质数 xx，如果按上文说的我们从 2x2x 开始标记其实是冗余的，应该直接从 x\cdot xx⋅x 开始标记，因为 2x,3x,\ldots2x,3x,… 这些数一定在 xx 之前就被其他数的倍数标记过了，例如 22 的所有倍数，33 的所有倍数等。

C++JavaJavaScriptGolangC

func countPrimes(n int) (cnt int) {
    isPrime := make([]bool, n)
    for i := range isPrime {
        isPrime[i] = true
    }
    for i := 2; i < n; i++ {
        if isPrime[i] {
            cnt++
            for j := 2 * i; j < n; j += i {
                isPrime[j] = false
            }
        }
    }
    return
}
复杂度分析

时间复杂度：O(n\log \log n)O(nloglogn)。具体证明这里不再展开，读者可以自行思考或者上网搜索，本质上是要求解 \sum_{p}\frac{n}{p}∑ 
p
​	
  
p
n
​	
  的和，其中 pp 为质数。当然我们可以了解这个算法一个比较松的上界 O(n\log n)O(nlogn) 怎么计算，这个等价于考虑 \sum_{i=1}^{n}\frac{n}{i}∑ 
i=1
n
​	
  
i
n
​	
  的和，而 O(\sum_{i=1}^{n}\frac{n}{i}) = O(n\sum_{i=1}^{n}\frac{1}{i})O(∑ 
i=1
n
​	
  
i
n
​	
 )=O(n∑ 
i=1
n
​	
  
i
1
​	
 )，而 11 到 nn 中所有数的倒数和趋近于 \log nlogn，因此 O(n\sum_{i=1}^{n}\frac{1}{i})=O(n\log n)O(n∑ 
i=1
n
​	
  
i
1
​	
 )=O(nlogn)。
空间复杂度：O(n)O(n)。我们需要 O(n)O(n) 的空间记录每个数是否为质数。
方法三：线性筛
此方法不属于面试范围范畴，本节只做简单讲解。

埃氏筛其实还是存在冗余的标记操作，比如对于 1515 这个数，它会同时被 3,53,5 两个数标记为合数，因此我们优化的目标是让每个合数只被标记一次，这样时间复杂度即能保证为 O(n)O(n)，这就是我们接下来要介绍的线性筛。

相较于埃氏筛，我们多维护一个 \textit{primes}primes 数组表示当前得到的质数集合。我们从小到大遍历，如果当前的数 xx 是质数，就将其加入 \textit{primes}primes 数组。

另一点与埃氏筛不同的是，「标记过程」不再仅当 xx 为质数时才进行，而是对每个整数 xx 都进行。对于整数 xx，我们不再标记其所有的倍数 x\cdot x,x\cdot (x+1),\ldotsx⋅x,x⋅(x+1),…，而是只标记质数集合中的数与 xx 相乘的数，即 \textit{primes}_0*x,\textit{primes}_1*x,\ldotsprimes 
0
​	
 ∗x,primes 
1
​	
 ∗x,…，且在发现 x\bmod \textit{primes}_i=0xmodprimes 
i
​	
 =0 的时候结束当前标记。

核心点在于：如果 xx 可以被 \textit{primes}_iprimes 
i
​	
  整除，那么对于合数 y=x\cdot \textit{primes}_{i+1}y=x⋅primes 
i+1
​	
  而言，它一定在后面遍历到 \frac{x}{\textit{primes}_i}\cdot\textit{primes}_{i+1} 
primes 
i
​	
 
x
​	
 ⋅primes 
i+1
​	
  这个数的时候会被标记，其他同理，这保证了每个合数只会被其「最小的质因数」筛去，即每个合数被标记一次。

线性筛还有其他拓展用途，有能力的读者可以搜索关键字「积性函数」继续探究如何利用线性筛来求解积性函数相关的题目。

C++JavaJavaScriptGolang

func countPrimes(n int) int {
    primes := []int{}
    isPrime := make([]bool, n)
    for i := range isPrime {
        isPrime[i] = true
    }
    for i := 2; i < n; i++ {
        if isPrime[i] {
            primes = append(primes, i)
        }
        for _, p := range primes {
            if i*p >= n {
                break
            }
            isPrime[i*p] = false
            if i%p == 0 {
                break
            }
        }
    }
    return len(primes)
}

int countPrimes(int n) {
    if (n < 2) {
        return 0;
    }
    int isPrime[n];
    int primes[n], primesSize = 0;
    memset(isPrime, 0, sizeof(isPrime));
    for (int i = 2; i < n; ++i) {
        if (!isPrime[i]) {
            primes[primesSize++] = i;
        }
        for (int j = 0; j < primesSize && i * primes[j] < n; ++j) {
            isPrime[i * primes[j]] = 1;
            if (i % primes[j] == 0) {
                break;
            }
        }
    }
    return primesSize;
}
复杂度分析

时间复杂度：O(n)O(n)。

空间复杂度：O(n)O(n)。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/count-primes/solution/ji-shu-zhi-shu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

