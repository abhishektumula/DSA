from abhishek import runtime
import time 
def generate_parenthesis(n : int ) -> list:
    res = []
    stack = []
    start = time.time()
    if  n == 0:
        return res 
    
    def backtracking(openN, closeN):
        if openN == closeN == n:
            res.append("".join(stack))
            return 
        
        if openN < n:
            stack.append("(")
            backtracking(openN+1, closeN)
            stack.pop()

        if closeN < openN:
            stack.append(")")
            backtracking(openN, closeN+1)
            stack.pop()

    backtracking(0, 0)
    end = time.time()
    print(runtime(start, end))
    return res 


print(generate_parenthesis(3))

        
