class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(deque)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        if self.tweets[userId]:
                heapq.heappush(heap, (-self.tweets[userId][0], 0, userId))

        for user in self.following[userId]:
            if self.tweets[user]:
                heapq.heappush(heap, (-self.tweets[user][0], 0, user))
        
        while heap and len(res) < 10:
            tweet, idx, user = heapq.heappop(heap)
            res.append(-tweet)
            if idx < len(self.tweets[user]) - 1:
                heapq.heappush(heap, (-self.tweets[user][idx + 1], idx + 1, user))
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
