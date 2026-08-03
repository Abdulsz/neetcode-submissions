class Solution {
    fun combine(n: Int, k: Int): List<List<Int>> {
        var res = mutableListOf<List<Int>>()
        var temp = mutableListOf<Int>()
        fun backtrack(i:Int){
            if (temp.size == k){
                res.add(temp.toList())
                return
            }
            for(j in i..n){
                temp.add(j)
                backtrack(j+1)
                temp.removeAt(temp.size-1)

            }

        }

        backtrack(1)
        return res
    }
}
