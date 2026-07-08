class Solution:
    def parseTernary(self, expression: str) -> str:
        
        stack = []

        for i in range(len(expression)-1,-1,-1):

            char = expression[i]
            
            if char == '?':
                
                tr = stack.pop()
                stack.pop()
                fa = stack.pop()

                if expression[i-1] == 'T':
                    stack.append(tr)
                else:
                    stack.append(fa)
                

            elif i+1 < len(expression) and expression[i+1]=='?':
                continue

            else:
                stack.append(char)

        return stack[0]
                

                