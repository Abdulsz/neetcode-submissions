class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []

        for i in range(len(expression)-1,-1,-1):
            c = expression[i]

            if c == '?':
                true = stack.pop()
                stack.pop()
                false = stack.pop()
                
                if expression[i-1] == 'T':
                    stack.append(true)
                else:
                    stack.append(false)
                continue
            if i+1 <len(expression) and expression[i+1] == '?':
                continue

            stack.append(c)

        return stack[0]

