class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        temps = [0]*len(temperatures)
        stack = []
        for i,num in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < num:
                idx = stack.pop()
                temps[idx] =  i-idx

            stack.append(i)

        return temps