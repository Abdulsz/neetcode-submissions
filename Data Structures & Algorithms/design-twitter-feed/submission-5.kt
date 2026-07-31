class Twitter { 
    var tweets = HashMap<Int,MutableList<Pair<Int,Int>>>()
    var timestamp = 0
    var follows = HashMap<Int,MutableSet<Int>>()

    fun postTweet(userId: Int, tweetId: Int) {

        tweets.getOrPut(userId){mutableListOf()}.add(Pair(timestamp,tweetId))
        timestamp+=1

    }

    fun getNewsFeed(userId: Int): List<Int> {

        /**
        - get userids followers
        - for each follower, find their latest tweet and add to maxHeap
        */

        var followees = follows.getOrPut(userId){hashSetOf()}
        followees.add(userId)
        var res = mutableListOf<Int>()

        var maxHeap = PriorityQueue<HeapEntry>{a,b ->b.timestamp.compareTo(a.timestamp)}

        for (f in followees){
            if (tweets.containsKey(f)){
                var lastIdx = tweets[f]!!.size-1
                var tweetId = tweets[f]!![lastIdx].second
                var time = tweets[f]!![lastIdx].first
                maxHeap.add(HeapEntry(time,tweetId,f,lastIdx-1))

            }
        }

        while (maxHeap.isNotEmpty() && res.size<10){
            val curr = maxHeap.poll()
            res.add(curr.tweetId)

            if (curr.index>=0){
                val (time,tweetId) = tweets[curr.followeeId]!![curr.index]
                maxHeap.add(HeapEntry(time,tweetId,curr.followeeId,curr.index-1))
            }
        }
        return res

    }

    fun follow(followerId: Int, followeeId: Int) {

        follows.getOrPut(followerId){mutableSetOf()}.add(followeeId)

    }

    fun unfollow(followerId: Int, followeeId: Int) {

        if(followerId != followeeId){
        follows[followerId]?.remove(followeeId)
        }

    }
    data class HeapEntry(
        val timestamp: Int,
        val tweetId: Int,
        val followeeId: Int,
        val index: Int
    )
}
