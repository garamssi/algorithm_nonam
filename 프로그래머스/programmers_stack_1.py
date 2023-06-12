# https://school.programmers.co.kr/learn/courses/30/lessons/12906
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

'''
def no_continuous(s):
    # 함수를 완성하세요
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))
'''