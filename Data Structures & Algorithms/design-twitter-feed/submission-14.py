class Twitter:

    def __init__(self):
        self.tweets = defaultdict(deque)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].appendleft(-tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        if userId not in self.following[userId]:
            self.following[userId].add(userId)

        for user in list(self.following[userId]):
            if len(self.tweets[user]) > 0:
                # push next tweet id, cur index, userId
                heapq.heappush(heap, (self.tweets[user][0], 0, user))
        
        while heap and len(res) < 10:
            tweet, idx, user = heapq.heappop(heap)
            res.append(-tweet)
            idx += 1
            if idx < len(self.tweets[user]):
                heapq.heappush(heap, (self.tweets[user][idx], idx, user))

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId: return None
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
