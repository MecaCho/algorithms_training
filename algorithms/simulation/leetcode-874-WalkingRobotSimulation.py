# encoding=utf8

'''
874. Walking Robot Simulation

A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.

Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).

Note:

North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.
 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 3 units to (3, 4).
The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
4. Turn left.
5. Move north 4 units to (1, 8).
The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.
Example 3:

Input: commands = [6,-1,-1,6], obstacles = []
Output: 36
Explanation: The robot starts at (0, 0):
1. Move north 6 units to (0, 6).
2. Turn right.
3. Turn right.
4. Move south 6 units to (0, 0).
The furthest point the robot ever gets from the origin is (0, 6), which squared is 62 = 36 units away.
 

Constraints:

1 <= commands.length <= 104
commands[i] is either -2, -1, or an integer in the range [1, 9].
0 <= obstacles.length <= 104
-3 * 104 <= xi, yi <= 3 * 104
The answer is guaranteed to be less than 231.

874. 模拟行走机器人

机器人在一个无限大小的 XY 网格平面上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：

    -2 ：向左转 90 度
    -1 ：向右转 90 度
    1 <= x <= 9 ：向前移动 x 个单位长度

在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。

机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，并继续执行下一个命令。

返回机器人距离原点的 最大欧式距离 的 平方 。（即，如果距离为 5 ，则返回 25 ）
 

注意：

    北方表示 +Y 方向。
    东方表示 +X 方向。
    南方表示 -Y 方向。
    西方表示 -X 方向。
    原点 [0,0] 可能会有障碍物。

 

示例 1：

输入：commands = [4,-1,3], obstacles = []
输出：25
解释：
机器人开始位于 (0, 0)：
1. 向北移动 4 个单位，到达 (0, 4)
2. 右转
3. 向东移动 3 个单位，到达 (3, 4)
距离原点最远的是 (3, 4) ，距离为 32 + 42 = 25

示例 2：

输入：commands = [4,-1,4,-2,4], obstacles = [[2,4]]
输出：65
解释：机器人开始位于 (0, 0)：
1. 向北移动 4 个单位，到达 (0, 4)
2. 右转
3. 向东移动 1 个单位，然后被位于 (2, 4) 的障碍物阻挡，机器人停在 (1, 4)
4. 左转
5. 向北走 4 个单位，到达 (1, 8)
距离原点最远的是 (1, 8) ，距离为 12 + 82 = 65

示例 3：

输入：commands = [6,-1,-1,6], obstacles = []
输出：36
解释：机器人开始位于 (0, 0):
1. 向北移动 6 个单位，到达 (0, 6).
2. 右转
3. 右转
4. 向南移动 6 个单位，到达 (0, 0).
机器人距离原点最远的点是 (0, 6)，其距离的平方是 62 = 36 个单位。

提示：

    1 <= commands.length <= 104
    commands[i] 的值可以取 -2、-1 或者是范围 [1, 9] 内的一个整数。
    0 <= obstacles.length <= 104
    -3 * 104 <= xi, yi <= 3 * 104
    答案保证小于 231
'''
