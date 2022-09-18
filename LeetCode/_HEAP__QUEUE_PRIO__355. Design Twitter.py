# Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

# Implement the Twitter class:

# Twitter() Initializes your twitter object.
# void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
# List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
# void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
# void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

# Example 1:

# Input
# ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
# [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
# Output
# [null, null, [5], null, null, [6, 5], null, [5]]

# Explanation
# Twitter twitter = new Twitter();
# twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
# twitter.follow(1, 2);    // User 1 follows user 2.
# twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
# twitter.unfollow(1, 2);  // User 1 unfollows user 2.
# twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

# Constraints:

# 1 <= userId, followerId, followeeId <= 500
# 0 <= tweetId <= 104
# All the tweets have unique IDs.
# At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.

from collections import deque

class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = []
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:        
        if userId not in self.users.keys():
            self.users[userId] = [userId] #followees = users who this users follows
        
        self.tweets.append([userId, tweetId])

    def getNewsFeed(self, userId: int):
        res = []
        i = len(self.tweets)-1
        while len(res)<10 and i>=0:
            if self.tweets[i][0] in self.users[userId]:
                res.append(self.tweets[i][1])
            i-=1
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users.keys():
            self.users[followerId]=[followerId]
        if followerId not in self.users.keys():
            self.users[followeeId]=[followeeId]

        self.users[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1, 5)
print(obj.getNewsFeed(1))
obj.follow(1, 2)
obj.follow(2, 1)
print(obj.getNewsFeed(2))
obj.postTweet(2, 6)
print(obj.getNewsFeed(1))
print(obj.getNewsFeed(2))
obj.unfollow(2, 1)
print(obj.getNewsFeed(1))
print(obj.getNewsFeed(2))
obj.unfollow(1, 2)
print(obj.getNewsFeed(1))
print(obj.getNewsFeed(2))