class Solution {
    fun longestDiverseString(a: Int, b: Int, c: Int): String {
        var count = mutableMapOf('a' to a, 'b' to b, 'c' to c)
        var maxHeap = PriorityQueue<Pair<Char,Int>>{a,b->b.second.compareTo(a.second)}
        for ((key,value) in count){
            if (value > 0){
                maxHeap.offer(Pair(key,value))
            }
        }
        var res = StringBuilder()

        while (maxHeap.isNotEmpty()){
            var(char1,cnt1) = maxHeap.poll()
            var len = res.length
            if(len >=2 && char1 == res[len-1] && char1 == res[len-2]){

                if(maxHeap.isEmpty()){
                    break
                }

                var(char2,cnt2) = maxHeap.poll()

                res.append(char2)
                cnt2-=1
                if (cnt2>0){
                    maxHeap.offer(Pair(char2,cnt2))
                }

                maxHeap.offer(Pair(char1,cnt1))
            }else{
                res.append(char1)
                cnt1-=1
                if (cnt1>0){
                    maxHeap.offer(Pair(char1,cnt1))
                }
            }
        }
        return res.toString()
    }
}
