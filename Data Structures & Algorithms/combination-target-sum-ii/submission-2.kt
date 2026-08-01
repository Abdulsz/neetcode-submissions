class Solution {
    fun combinationSum2(candidates: IntArray, target: Int): List<List<Int>> {
        var res = mutableListOf<List<Int>>()
        var current = mutableListOf<Int>()
        candidates.sort()
        fun backtrack(i:Int,total:Int){
            if (total == target){
                res.add(current.toList())
                return
            }
            if (i==candidates.size || total>target){
                return
            }

            current.add(candidates[i])
            backtrack(i+1,total+candidates[i])

            current.removeAt(current.size-1)
            var nextIdx = i
            while (nextIdx+1<candidates.size && candidates[nextIdx] == candidates[nextIdx+1]){
                nextIdx+=1
            }
            backtrack(nextIdx+1,total)
            
        }
        backtrack(0,0)
        return res
    }
}
