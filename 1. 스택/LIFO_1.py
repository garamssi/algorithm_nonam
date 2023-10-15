def isValid(s) :

    stack = []
 
    # 여는 값이면 반대 되는 값을 넣어주고, 스택이 비워있지 않고 닫힌 값이 나오면
    # 스택의 마지막 값을 꺼내와서 해당 값과 똑같은지 비교한다.
    # 똑같지 않으면 False, 스택의 값이 남아 있어도 False
    for p in s :
        if p == "{" :
            stack.append("}")
        elif p in "(" :
            stack.append(")")
        elif p == "[" :
            stack.append("]")
        elif not stack or stack.pop() != p :
            return False
    
    return not stack

print(isValid("[][]{}"));


