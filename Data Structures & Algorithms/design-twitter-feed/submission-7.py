class Twitter:

    def __init__(self):
        
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp,tweetId))
        self.timestamp+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        userList = set(self.followers[userId])
        userList.add(userId)
        maxHeap = []
        for u in userList:
            if u not in self.tweets:
                continue
            time,tweet = self.tweets[u][-1]
            size = len(self.tweets[u])
            heapq.heappush(maxHeap,(-time,tweet,u,size-2))

        while maxHeap and len(feed)<10:
            t,tweet,user,lastIdx = heapq.heappop(maxHeap)
            feed.append(tweet)

            if lastIdx >=0:
                nxtTime,nxtTweet = self.tweets[user][lastIdx]
                heapq.heappush(maxHeap,(-nxtTime,nxtTweet,user,lastIdx-1))
        
        return feed
                      


        

    def follow(self, followerId: int, followeeId: int) -> None:

        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:

        if followeeId not in self.followers[followerId]:
            return
        
        self.followers[followerId].remove(followeeId)
        
