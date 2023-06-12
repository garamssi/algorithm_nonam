# def rotateQue(n, m, k):
#     size = m
#     cnt = 0
#     index = 0
#     arr = []

#     for i in range(1, n+1):
#         arr.append(i)

#     while size > 0:
#         result = 0

#         if k[index] <= len(arr) // 2:
#             result = arr.index(k[index])
#             arr.pop(result)
#             print("상단 : ", result)
#         else:
#             result = arr[::-1].index(k[index])
#             target = arr[::-1].pop(result)
#             arr.remove(target)
#             print("하단 : ", result)

#             if result != 0 :
#                 result += 1

#         print(arr)
#         cnt += result
#         index += 1
#         size -= 1
    
#     return cnt
# print(rotateQue(10, 2, [1,10]))
# print(rotateQue(10, 3, [1,2,3])) # 0
# print(rotateQue(10, 3, [2,9,5])) # 8
# print(rotateQue(36, 6, [27, 16, 30, 11, 6, 23])) # 59
# print(rotateQue(10, 10, [1, 6, 3, 2, 7, 9, 8, 4, 10, 5])) # 14

# list = [ 1,2,3,4]
# list[::-1].pop()
# print(list)

from collections import deque

# 입력 받기
N, M = map(int, input().split())
positions = list(map(int, input().split()))

# 큐 초기화
queue = deque(range(1, N + 1))

# 뽑아내려는 원소들을 차례대로 처리
moves = 0
for pos in positions:
    # 원소가 현재 큐의 맨 앞에 있는 경우
    if queue[0] == pos:
        queue.popleft()
        continue
    
    # 원소의 위치를 찾아서 왼쪽 또는 오른쪽으로 이동
    idx = queue.index(pos)
    if idx <= len(queue) // 2:
        # 왼쪽으로 이동
        moves += idx
        queue.rotate(-idx)
    else:
        # 오른쪽으로 이동
        moves += len(queue) - idx
        queue.rotate(len(queue) - idx)

# 결과 출력
print(moves)