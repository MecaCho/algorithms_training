'''
1279. 红绿灯路口
这是两条路的交叉路口。第一条路是 A 路，车辆可沿 1 号方向由北向南行驶，也可沿 2 号方向由南向北行驶。第二条路是 B 路，车辆可沿 3 号方向由西向东行驶，也可沿 4 号方向由东向西行驶。



每条路在路口前都有一个红绿灯。红绿灯可以亮起红灯或绿灯。

绿灯表示两个方向的车辆都可通过路口。
红灯表示两个方向的车辆都不可以通过路口，必须等待绿灯亮起。
两条路上的红绿灯不可以同时为绿灯。这意味着，当 A 路上的绿灯亮起时，B 路上的红灯会亮起；当 B 路上的绿灯亮起时，A 路上的红灯会亮起.

开始时，A 路上的绿灯亮起，B 路上的红灯亮起。当一条路上的绿灯亮起时，所有车辆都可以从任意两个方向通过路口，直到另一条路上的绿灯亮起。不同路上的车辆不可以同时通过路口。

给这个路口设计一个没有死锁的红绿灯控制系统。

实现函数 void carArrived(carId, roadId, direction, turnGreen, crossCar) :

carId 为到达车辆的编号。
roadId 为车辆所在道路的编号。
direction 为车辆的行进方向。
turnGreen 是一个函数，调用此函数会使当前道路上的绿灯亮起。
crossCar 是一个函数，调用此函数会允许车辆通过路口。
当你的答案避免了车辆在路口出现死锁，此答案会被认定为正确的。当路口已经亮起绿灯时仍打开绿灯，此答案会被认定为错误的。



示例 1:

输入: cars = [1,3,5,2,4], directions = [2,1,2,4,3], arrivalTimes = [10,20,30,40,50]
输出: [
"Car 1 Has Passed Road A In Direction 2",    // A 路上的红绿灯为绿色，1 号车可通过路口。
"Car 3 Has Passed Road A In Direction 1",    // 红绿灯仍为绿色，3 号车通过路口。
"Car 5 Has Passed Road A In Direction 2",    // 红绿灯仍为绿色，5 号车通过路口。
"Traffic Light On Road B Is Green",          // 2 号车在 B 路请求绿灯。
"Car 2 Has Passed Road B In Direction 4",    // B 路上的绿灯现已亮起，2 号车通过路口。
"Car 4 Has Passed Road B In Direction 3"     // 红绿灯仍为绿色，4 号车通过路口。
]
示例 2:

输入: cars = [1,2,3,4,5], directions = [2,4,3,3,1], arrivalTimes = [10,20,30,40,40]
输出: [
"Car 1 Has Passed Road A In Direction 2",    // A 路上的红绿灯为绿色，1 号车可通过路口。
"Traffic Light On Road B Is Green",          // 2 号车在 B 路请求绿灯。
"Car 2 Has Passed Road B In Direction 4",    // B 路上的绿灯现已亮起，2 号车通过路口。
"Car 3 Has Passed Road B In Direction 3",    // B 路上的绿灯现已亮起，3 号车通过路口。
"Traffic Light On Road A Is Green",          // 5 号车在 A 路请求绿灯。
"Car 5 Has Passed Road A In Direction 1",    // A 路上的绿灯现已亮起，5 号车通过路口。
"Traffic Light On Road B Is Green",          // 4 号车在 B 路请求绿灯。4 号车在路口等灯，直到 5 号车通过路口，B 路的绿灯亮起。
"Car 4 Has Passed Road B In Direction 3"     // B 路上的绿灯现已亮起，4 号车通过路口。
]
解释: 这是一个无死锁的方案。注意，在 A 路上的绿灯亮起、5 号车通过前让 4 号车通过，也是一个正确且可被接受的方案。


提示：

1 <= cars.length <= 20
cars.length = directions.length
cars.length = arrivalTimes.length
cars 中的所有值都是唯一的。
1 <= directions[i] <= 4
arrivalTimes 是非递减的。

1279. Traffic Light Controlled Intersection
There is an intersection of two roads. First road is road A where cars travel from North to South in direction 1 and from South to North in direction 2. Second road is road B where cars travel from West to East in direction 3 and from East to West in direction 4.



There is a traffic light located on each road before the intersection. A traffic light can either be green or red.

Green means cars can cross the intersection in both directions of the road.
Red means cars in both directions cannot cross the intersection and must wait until the light turns green.
The traffic lights cannot be green on both roads at the same time. That means when the light is green on road A, it is red on road B and when the light is green on road B, it is red on road A.

Initially, the traffic light is green on road A and red on road B. When the light is green on one road, all cars can cross the intersection in both directions until the light becomes green on the other road. No two cars traveling on different roads should cross at the same time.

Design a deadlock-free traffic light controlled system at this intersection.

Implement the function void carArrived(carId, roadId, direction, turnGreen, crossCar) where:

carId is the id of the car that arrived.
roadId is the id of the road that the car travels on.
direction is the direction of the car.
turnGreen is a function you can call to turn the traffic light to green on the current road.
crossCar is a function you can call to let the current car cross the intersection.
Your answer is considered correct if it avoids cars deadlock in the intersection. Turning the light green on a road when it was already green is considered a wrong answer.



Example 1:

Input: cars = [1,3,5,2,4], directions = [2,1,2,4,3], arrivalTimes = [10,20,30,40,50]
Output: [
"Car 1 Has Passed Road A In Direction 2",    // Traffic light on road A is green, car 1 can cross the intersection.
"Car 3 Has Passed Road A In Direction 1",    // Car 3 crosses the intersection as the light is still green.
"Car 5 Has Passed Road A In Direction 2",    // Car 5 crosses the intersection as the light is still green.
"Traffic Light On Road B Is Green",          // Car 2 requests green light for road B.
"Car 2 Has Passed Road B In Direction 4",    // Car 2 crosses as the light is green on road B now.
"Car 4 Has Passed Road B In Direction 3"     // Car 4 crosses the intersection as the light is still green.
]
Example 2:

Input: cars = [1,2,3,4,5], directions = [2,4,3,3,1], arrivalTimes = [10,20,30,40,40]
Output: [
"Car 1 Has Passed Road A In Direction 2",    // Traffic light on road A is green, car 1 can cross the intersection.
"Traffic Light On Road B Is Green",          // Car 2 requests green light for road B.
"Car 2 Has Passed Road B In Direction 4",    // Car 2 crosses as the light is green on road B now.
"Car 3 Has Passed Road B In Direction 3",    // Car 3 crosses as the light is green on road B now.
"Traffic Light On Road A Is Green",          // Car 5 requests green light for road A.
"Car 5 Has Passed Road A In Direction 1",    // Car 5 crosses as the light is green on road A now.
"Traffic Light On Road B Is Green",          // Car 4 requests green light for road B. Car 4 blocked until car 5 crosses and then traffic light is green on road B.
"Car 4 Has Passed Road B In Direction 3"     // Car 4 crosses as the light is green on road B now.
]
Explanation: This is a dead-lock free scenario. Note that the scenario when car 4 crosses before turning light into green on road A and allowing car 5 to pass is also correct and Accepted scenario.


Constraints:

1 <= cars.length <= 20
cars.length = directions.length
cars.length = arrivalTimes.length
All values of cars are unique
1 <= directions[i] <= 4
arrivalTimes is non-decreasing
'''



class TrafficLight(object):

    def __init__(self):
        self.green1 = True
        self.green2 = False
        self.lock = True

    def carArrived(self, carId, roadId, direction, turnGreen, crossCar):
        """
        :type roadId: int --> // ID of the car
        :type carId: int --> // ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
        :type direction: int --> // Direction of the car
        :type turnGreen: method --> // Use turnGreen() to turn light to green on current road
        :type crossCar: method --> // Use crossCar() to make car cross the intersection
        :rtype: void
        """
        if self.lock:
            self.lock = False

            if not self.green1 and roadId == 1:
                turnGreen()
                self.green1 = True
                self.green2 = False
            if not self.green2 and roadId == 2:
                turnGreen()
                self.green2 = True
                self.green1 = False

            crossCar()

            self.lock = True
