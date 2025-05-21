import time 
from abhishek import runtime
def valid_parenthesis(param : str ) -> bool:
    start_time = time.time()
    opening = ['(', "{", "["]
    stack = []
    for each in param:
        if each in opening:
            stack.append(each)
        else:
            if each == "}" and stack[-1] == "{":
                stack.pop()
            elif each == "]" and stack[-1] == "[":
                stack.pop()
            elif each == ")" and stack[-1] == "(":
                stack.pop()
            else:
                end_time = time.time()
                print(runtime(start_time, end_time))
                return False 
    end_time = time.time()
    print(runtime(start_time, end_time))
    return not stack


print(valid_parenthesis("{{}}()"))
print(valid_parenthesis("{{{{}"))

                    

