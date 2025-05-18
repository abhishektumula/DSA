#approach : using stack
import time
def valid_parentheses(parn : str)-> bool:
    stack = []
    opening = ["[","{","("]
    start_time = time.time()
    for each in parn:
        if each in opening:
            stack.append(each)
        else:
            if not stack:
                end_time = time.time()
                print(f"runtime:{(end_time - start_time)*1000:.3f}")
                return False 
            else:
                if each == "}" and stack[-1] == "{":
                    stack.pop()
                if each == ")" and stack[-1] == "(":
                    stack.pop()
                if each == "]" and stack[-1] == "[":
                    stack.pop()

    end_time = time.time()
    print(f"runtime:{(end_time - start_time)*1000:.3f}")
    return True if not stack else False
print(valid_parentheses("[[]"))
