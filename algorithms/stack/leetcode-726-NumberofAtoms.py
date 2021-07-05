# encoding=utf8

'''
726. Number of Atoms
Given a chemical formula (given as a string), return the count of each atom.

The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:

Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.
Example 2:

Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
Example 3:

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
Example 4:

Input: formula = "Be32"
Output: "Be32"
 

Constraints:

1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.

726. 原子的数量
给定一个化学式formula（作为字符串），返回每种原子的数量。

原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。

两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。

一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。

给定一个化学式 formula ，返回所有原子的数量。格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

 

示例 1：

输入：formula = "H2O"
输出："H2O"
解释：
原子的数量是 {'H': 2, 'O': 1}。
示例 2：

输入：formula = "Mg(OH)2"
输出："H2MgO2"
解释： 
原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
示例 3：

输入：formula = "K4(ON(SO3)2)2"
输出："K4N2O14S4"
解释：
原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
示例 4：

输入：formula = "Be32"
输出："Be32"
 

提示：

1 <= formula.length <= 1000
formula 由小写英文字母、数字 '(' 和 ')' 组成。
formula 是有效的化学式。
'''

# golang solution

'''
func countOfAtoms(formula string) string {
    i, n := 0, len(formula)

    parseAtom := func() string {
        start := i
        i++ // 扫描，跳过首字母
        for i < n && unicode.IsLower(rune(formula[i])) { 
            i++ // 扫描首字母后的小写字母
        }
        return formula[start:i]
    }

    parseNum := func() (num int) {
        if i == n || !unicode.IsDigit(rune(formula[i])) { 
            return 1 // 不是数字，视作 1
        }
        for ; i < n && unicode.IsDigit(rune(formula[i])); i++ { 
            num = num*10 + int(formula[i]-'0') // 扫描数字
        }
        return
    }

    stk := []map[string]int{{}}
    for i < n {
        if ch := formula[i]; ch == '(' {
            i++
            stk = append(stk, map[string]int{}) // 将一个空的哈希表压入栈中，准备统计括号内的原子数量
        } else if ch == ')' {
            i++
            num := parseNum() // 括号右侧数字
            atomNum := stk[len(stk)-1]
            stk = stk[:len(stk)-1] // 弹出括号内的原子数量
            for atom, v := range atomNum {
                stk[len(stk)-1][atom] += v * num // 将括号内的原子数量乘上 num，加到上一层的原子数量中
            }
        } else {
            atom := parseAtom()
            num := parseNum()
            stk[len(stk)-1][atom] += num // 统计原子数量
        }
    }

    atomNum := stk[0]
    type pair struct {
        atom string
        num  int
    }
    pairs := make([]pair, 0, len(atomNum))
    for k, v := range atomNum {
        pairs = append(pairs, pair{k, v})
    }
    sort.Slice(pairs, func(i, j int) bool { return pairs[i].atom < pairs[j].atom })

    ans := []byte{}
    for _, p := range pairs {
        ans = append(ans, p.atom...)
        if p.num > 1 {
            ans = append(ans, strconv.Itoa(p.num)...)
        }
    }
    return string(ans)
}
'''
