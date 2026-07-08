from collections import defaultdict
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> [(time, tweetId)]
        self.followMap = defaultdict(set)    # followerId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        # 新闻流来源：自己 + 自己关注的人
        users = set(self.followMap[userId])
        users.add(userId)

        # 把每个用户的最新一条推文放进堆
        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                time, tweetId = self.tweets[uid][idx]

                # Python 是小根堆，所以用 -time 表示越新的推文越先弹出
                heapq.heappush(heap, (-time, tweetId, uid, idx))

        # 最多取 10 条
        while heap and len(res) < 10:
            negTime, tweetId, uid, idx = heapq.heappop(heap)
            res.append(tweetId)

            # 如果这个用户还有更早的推文，把上一条也放入堆
            if idx > 0:
                prevIdx = idx - 1
                time, prevTweetId = self.tweets[uid][prevIdx]
                heapq.heappush(heap, (-time, prevTweetId, uid, prevIdx))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)