# encoding=utf8

'''
5430. 设计浏览器历史记录
你有一个只支持单个标签页的 浏览器 ，最开始你浏览的网页是 homepage ，你可以访问其他的网站 url ，也可以在浏览历史中后退 steps 步或前进 steps 步。

请你实现 BrowserHistory 类：

BrowserHistory(string homepage) ，用 homepage 初始化浏览器类。
void visit(string url) 从当前页跳转访问 url 对应的页面  。执行此操作会把浏览历史前进的记录全部删除。
string back(int steps) 在浏览历史中后退 steps 步。如果你只能在浏览历史中后退至多 x 步且 steps > x ，那么你只后退 x 步。请返回后退 至多 steps 步以后的 url 。
string forward(int steps) 在浏览历史中前进 steps 步。如果你只能在浏览历史中前进至多 x 步且 steps > x ，那么你只前进 x 步。请返回前进 至多 steps步以后的 url 。


示例：

输入：
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
输出：
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

解释：
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // 你原本在浏览 "leetcode.com" 。访问 "google.com"
browserHistory.visit("facebook.com");     // 你原本在浏览 "google.com" 。访问 "facebook.com"
browserHistory.visit("youtube.com");      // 你原本在浏览 "facebook.com" 。访问 "youtube.com"
browserHistory.back(1);                   // 你原本在浏览 "youtube.com" ，后退到 "facebook.com" 并返回 "facebook.com"
browserHistory.back(1);                   // 你原本在浏览 "facebook.com" ，后退到 "google.com" 并返回 "google.com"
browserHistory.forward(1);                // 你原本在浏览 "google.com" ，前进到 "facebook.com" 并返回 "facebook.com"
browserHistory.visit("linkedin.com");     // 你原本在浏览 "facebook.com" 。 访问 "linkedin.com"
browserHistory.forward(2);                // 你原本在浏览 "linkedin.com" ，你无法前进任何步数。
browserHistory.back(2);                   // 你原本在浏览 "linkedin.com" ，后退两步依次先到 "facebook.com" ，然后到 "google.com" ，并返回 "google.com"
browserHistory.back(7);                   // 你原本在浏览 "google.com"， 你只能后退一步到 "leetcode.com" ，并返回 "leetcode.com"


提示：

1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage 和 url 都只包含 '.' 或者小写英文字母。
最多调用 5000 次 visit， back 和 forward 函数。


5430. Design Browser History
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.


Example:

Input:
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
Output:
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

Explanation:
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"


Constraints:

1 <= homepage.length <= 20
1 <= url.length <= 20
1 <= steps <= 100
homepage and url consist of  '.' or lower case English letters.
At most 5000 calls will be made to visit, back, and forward.
'''


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.pages = [homepage]
        self.loc = 0


    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        if self.loc is None or self.loc == len(self.pages) - 1:
            self.pages.append(url)
            self.loc = len(self.pages) - 1
        else:
            self.pages = self.pages[:self.loc +1] + [url]
            self.loc += 1
        # print(self.pages, self.loc)



    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.loc - steps < 0:
            self.loc = 0
        else:
            self.loc -= steps
        # print(self.loc)
        return self.pages[self.loc]



    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if (steps + self.loc) >= len(self.pages):
            self.loc = len(self.pages) - 1
        else:
            self.loc += steps
        # print(self.loc)
        return self.pages[self.loc]



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)


# golang

'''
type BrowserHistory struct {
	Pages []string
	Loc int

}


func Constructor(homepage string) BrowserHistory {

	pages := []string{homepage}

	return BrowserHistory{pages, 0}

}


func (this *BrowserHistory) Visit(url string)  {
	if this.Loc == len(this.Pages) - 1{
		this.Pages = append(this.Pages, url)
	}else {
		this.Pages = this.Pages[:this.Loc+1]
		this.Pages = append(this.Pages, url)
	}
    this.Loc++
	// fmt.Println(this.Pages)
}


func (this *BrowserHistory) Back(steps int) string {
	if this.Loc - steps < 0{
		this.Loc = 0
	}else {
		this.Loc -= steps
	}
	return this.Pages[this.Loc]
}


func (this *BrowserHistory) Forward(steps int) string {
	if this.Loc + steps > len(this.Pages) - 1 {
		this.Loc = len(this.Pages) - 1
	}else {
		this.Loc += steps
	}
	return this.Pages[this.Loc]
}


/**
 * Your BrowserHistory object will be instantiated and called as such:
 * obj := Constructor(homepage);
 * obj.Visit(url);
 * param_2 := obj.Back(steps);
 * param_3 := obj.Forward(steps);
 */
'''

# tips

'''

Use two stack one for back history and one for forward history and simulate the functions.

Can you do faster by using different data structure ?
'''
