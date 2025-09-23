def validParenths(oper: str) -> bool:
    opening = ["(", "{", "["]
    closing = [")", "}", "]"]
    stack = []
    for each in oper:
        if each in opening:
            stack.append(each)
        else:
            if stack:
                if each == ")" and stack[-1] == "(":
                    stack.pop()
                elif each == "}" and stack[-1] == "{":
                    stack.pop()
                elif each == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            else:
                return False

    return True if not stack else False
