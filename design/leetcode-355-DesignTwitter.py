'''
355. 设计推特
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户
示例:

Twitter twitter = new Twitter();

// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1);

// 用户1关注了用户2.
twitter.follow(1, 2);

// 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6);

// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
// 推文id6应当在推文id5之前，因为它是在5之后发送的.
twitter.getNewsFeed(1);

// 用户1取消关注了用户2.
twitter.unfollow(1, 2);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
// 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1);

355. Design Twitter
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);

'''

class Tweet():
    def __init__(self, user_id, t_id, update_time):
        self.user_id = user_id
        self.t_id = t_id
        self.update_time = update_time

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.tweets = collections.defaultdict(list)
        self.time_ = 0
        self.fellows = collections.defaultdict(list)


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        # print(self.tweets, userId, tweetId)
        self.time_ += 1
        # new_tweet = Tweet(userId, tweetId, self.time_)
        new_tweet = (userId, tweetId, self.time_)
        self.tweets[userId].append(new_tweet)
        # print(self.tweets)


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        # print(self.tweets)
        tweets = [i for i in self.tweets[userId]]
        # print(tweets)
        for user_id in self.fellows[userId]:
            # print(user_id)
            if user_id != userId:
                tweets.extend(self.tweets[user_id])
        # print(tweets)
        tweets = sorted(tweets, key=lambda x:x[2], reverse=True)
        # print(tweets)
        res = [i[1] for i in tweets]
        # print(res)
        return res[:10]



    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId not in self.fellows[followerId]:
            self.fellows[followerId].append(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # print(self.fellows, followerId, followeeId)
        if self.fellows[followerId] and followeeId in self.fellows[followerId]:
            self.fellows[followerId].remove(followeeId)
        # print(self.fellows, followerId, followeeId)




# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# 执行用时 :
# 76 ms
# , 在所有 Python 提交中击败了
# 100.00%
# 的用户
# 内存消耗 :
# 19 MB
# , 在所有 Python 提交中击败了
# 50.00%
# 的用户


# 执行用时 :
# 88 ms
# , 在所有 Python 提交中击败了
# 75.61%
# 的用户
# 内存消耗 :
# 19 MB
# , 在所有 Python 提交中击败了
# 50.00%
# 的用户
# without defaultdict
class Twitter1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        import collections
        self.tweets = {}
        self.time_ = 0
        self.fellows = {}


    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """

        self.time_ += 1
        new_tweet = (userId, tweetId, self.time_)
        if userId in self.tweets:
            self.tweets[userId].append(new_tweet)
        else:
            self.tweets[userId] = [new_tweet]


    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tweets = []
        if userId in self.tweets:
            tweets = [i for i in self.tweets[userId]]
        if self.fellows and userId in self.fellows:
            for user_id in self.fellows[userId]:
                if user_id != userId:
                    # add_tweets = []
                    if user_id in self.tweets:
                        tweets.extend(self.tweets[user_id])
        tweets = sorted(tweets, key=lambda x:x[2], reverse=True)
        res = [i[1] for i in tweets]
        return res[:10]



    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.fellows:
            self.fellows[followerId] = [followeeId]
            return
        if followeeId not in self.fellows[followerId]:
            self.fellows[followerId].append(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.fellows and self.fellows[followerId] and followeeId in self.fellows[followerId]:
            self.fellows[followerId].remove(followeeId)




# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

if __name__ == '__main__':
    # ["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
    # [[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]
    print(1)