class Solution {
    fun carPooling(trips: Array<IntArray>, capacity: Int): Boolean {
        trips.sortBy{it[1]}
        var curr = 0
        var minHeap = PriorityQueue<Pair<Int,Int>>{a,b->a.first.compareTo(b.first)}
        for (i in 0 until trips.size){
            var(num,fr,t) = trips[i]
            curr+=num
            
                while(minHeap.isNotEmpty() && minHeap.peek().first <= fr){
                    var(prevTo,passCnt) = minHeap.poll()
                    curr-=passCnt
                }
                
            
            if (curr>capacity){
                return false
            }
            minHeap.offer(Pair(t,num))
        }
        return true
    }
}
