class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        window = 0
        max_win = 0
        l = 0
        res = 0

        for r in range(len(customers)):

            if grumpy[r]:
                window+=customers[r]

            else:
                res+= customers[r]

            if r-l+1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l+=1

            max_win = max(max_win, window)

        return max_win+res

            

