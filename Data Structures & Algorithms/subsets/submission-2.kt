class Solution {
    fun subsets(nums: IntArray): List<List<Int>> {
        var res = mutableListOf<List<Int>>()
        var temp = mutableListOf<Int>()
        fun backtrack(i:Int){
            if (i>=nums.size){
                res.add(temp.toList())
                return
            }

            temp.add(nums[i])
            backtrack(i+1)
            temp.removeAt(temp.size-1)
            backtrack(i+1)
        }
        backtrack(0)
        return res
        

    }
}
