class Solution {
    fun exist(board: Array<CharArray>, word: String): Boolean {
        val rows = board.size
        val cols = board[0].size
        var visited = mutableSetOf<Pair<Int,Int>>()

        fun dfs(r:Int,c:Int,i:Int):Boolean{
            if (i==word.length){
                return true
            }

            if (i>word.length || r<0 || r>=rows || c<0 || c>=cols || Pair(r,c) in visited || board[r][c] != word[i]){
                return false
            }

            visited.add(Pair(r,c))
            val res = dfs(r+1,c,i+1) || dfs(r-1,c,i+1) || dfs(r,c+1,i+1) || dfs(r,c-1,i+1)
            visited.remove(Pair(r,c))

            return res
        }

        for(r in 0 until rows){
            for(c in 0 until cols){
                if (dfs(r,c,0)){
                    return true
                }
            }
        }
        return false
    }
}
