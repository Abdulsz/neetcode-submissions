class Solution {
    fun permute(nums: IntArray): List<List<Int>> {

        var res = mutableListOf<List<Int>>()
        var temp = mutableListOf<Int>()

        fun backtrack(){

            if(temp.size == nums.size){
                res.add(temp.toList())
                return 
            }
            for(j in 0 until nums.size){
                if (!temp.contains(nums[j])){
                    temp.add(nums[j])
                    backtrack()
                    temp.removeAt(temp.size-1)
                }
            }
            
        }
        backtrack()
        return res
    }
}
