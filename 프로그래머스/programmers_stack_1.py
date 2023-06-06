def solution(arr):
    if not arr :
        return []
    
    answer = []
    for i in arr :
        if not answer :
            answer.append(i)
        elif i == answer[-1] :
            answer.pop()
            answer.append(i)
        else :
            answer.append(i)
            

    return answer

result = solution(arr = [4,4,4,3,3])
print(result)
