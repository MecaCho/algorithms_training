# encoding=utf8


'''
2034. Stock Price Fluctuation 
You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
Finds the maximum price the stock has been based on the current records.
Finds the minimum price the stock has been based on the current records.
Implement the StockPrice class:

StockPrice() Initializes the object with no price records.
void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
int current() Returns the latest price of the stock.
int maximum() Returns the maximum price of the stock.
int minimum() Returns the minimum price of the stock.
 

Example 1:

Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.
 

Constraints:

1 <= timestamp, price <= 109
At most 105 calls will be made in total to update, current, maximum, and minimum.
current, maximum, and minimum will be called only after update has been called at least once.

'''


class StockPrice(object):

    def __init__(self):
        from sortedcontainers import SortedList
        self.price = SortedList()
        self.timePriceMap = {}
        self.maxTimestamp = 0

    def update(self, timestamp, price):
        """
        :type timestamp: int
        :type price: int
        :rtype: None
        """
        if timestamp in self.timePriceMap:
            self.price.discard(self.timePriceMap[timestamp])
        self.price.add(price)
        self.timePriceMap[timestamp] = price
        self.maxTimestamp = max(self.maxTimestamp, timestamp)


    def current(self):
        """
        :rtype: int
        """
        return self.timePriceMap[self.maxTimestamp]



    def maximum(self):
        """
        :rtype: int
        """
        return self.price[-1]


    def minimum(self):
        """
        :rtype: int
        """
        return self.price[0]



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()




class StockPrice:

    def __init__(self):
        import sortedcontainers
        self.prices = sortedcontainers.SortedList()
        self.prices_map = {}
        self.max_time = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp in self.prices_map:
            self.prices.discard(self.prices_map[timestamp])
        self.prices.add(price)

        self.prices_map[timestamp] = price
        self.max_time = max(self.max_time, timestamp)


    def current(self) -> int:
        return self.prices_map[self.max_time]

    def maximum(self) -> int:
        return self.prices[-1]

    def minimum(self) -> int:
        return self.prices[0]


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()


