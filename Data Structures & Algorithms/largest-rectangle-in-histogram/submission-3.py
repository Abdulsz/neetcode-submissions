class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        maxArea = 0
        for i,hei in enumerate(heights):

            start = i
            while stack and stack[-1][1] > hei:
                idx,h = stack.pop()
                maxArea = max(maxArea,(i-idx)*h)
            
                start = idx

            stack.append((start,hei))

        for i,h in stack:
            maxArea = max(maxArea,(len(heights)-i)*h)

        return maxArea

