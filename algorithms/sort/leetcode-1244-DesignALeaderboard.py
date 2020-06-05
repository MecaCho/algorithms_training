

'''
1244. 力扣排行榜
新一轮的「力扣杯」编程大赛即将启动，为了动态显示参赛者的得分数据，需要设计一个排行榜 Leaderboard。

请你帮忙来设计这个 Leaderboard 类，使得它有如下 3 个函数：

addScore(playerId, score)：
假如参赛者已经在排行榜上，就给他的当前得分增加 score 点分值并更新排行。
假如该参赛者不在排行榜上，就把他添加到榜单上，并且将分数设置为 score。
top(K)：返回前 K 名参赛者的 得分总和。
reset(playerId)：将指定参赛者的成绩清零。题目保证在调用此函数前，该参赛者已有成绩，并且在榜单上。
请注意，在初始状态下，排行榜是空的。



示例 1：

输入：
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
输出：
[null,null,null,null,null,null,73,null,null,null,141]

解释：
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;


提示：

1 <= playerId, K <= 10000
题目保证 K 小于或等于当前参赛者的数量
1 <= score <= 100
最多进行 1000 次函数调用

1244. Design A Leaderboard
Design a Leaderboard class, which has 3 functions:

addScore(playerId, score): Update the leaderboard by adding score to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given score.
top(K): Return the score sum of the top K players.
reset(playerId): Reset the score of the player with the given id to 0 (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.
Initially, the leaderboard is empty.



Example 1:

Input:
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output:
[null,null,null,null,null,null,73,null,null,null,141]

Explanation:
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);   // leaderboard = [[1,73]];
leaderboard.addScore(2,56);   // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);   // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);   // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);    // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);           // returns 73;
leaderboard.reset(1);         // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);         // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);   // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);           // returns 141 = 51 + 51 + 39;


Constraints:

1 <= playerId, K <= 10000
It's guaranteed that K is less than or equal to the current number of players.
1 <= score <= 100
There will be at most 1000 function calls.
'''

# golang

'''
type Leaderboard struct {
	scores map[int]int
}


func Constructor() Leaderboard {
	scores := make(map[int]int, 1)
	b := Leaderboard{scores}
	return  b
}


func (this *Leaderboard) AddScore(playerId int, score int)  {
	if _, ok := this.scores[playerId]; ok{
		this.scores[playerId] += score
	}else {
		this.scores[playerId] = score
	}
}


func (this *Leaderboard) Top(K int) int {
	
	allScores := []int{}
	
	for k, _ := range this.scores{
		allScores = append(allScores, this.scores[k])
	}
	
	sort.Ints(allScores)
	
	res := 0
	for i := 0; i < K; i++{
		res += allScores[len(allScores) - 1 - i]
	}
	
	return res
}


func (this *Leaderboard) Reset(playerId int)  {
	this.scores[playerId] = 0
}


/**
 * Your Leaderboard object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddScore(playerId,score);
 * param_2 := obj.Top(K);
 * obj.Reset(playerId);
 */
'''

# tips

'''
What data structure can we use to keep the players' data?

Keep a map (dictionary) of player scores.

For each top(K) function call, find the maximum K scores and add them.
'''