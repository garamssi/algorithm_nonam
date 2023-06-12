from collections import deque

def solution(grid):
    result_len = -1
    row = len(grid)
    col = len(grid[0])
    visited =[[False] * col for _ in range(row)]


    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = True

    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        cur_r, cur_c, cur_len = queue.popleft()
        # 목적지에 도착했을 떄 그때의 cur_len을 result_len에 저장하면 된다.
        if cur_r == row - 1 and cur_c == col - 1:
            result_len = cur_len
            break

        # 연결되어 있는 vertext 확인하기
        for dr, dc in delta:
            next_r = cur_r + dr
            next_c = cur_c + dc
            if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
                # 목적지가 1일 경우 and 방문하지 않았다면
                if grid[next_r][next_c] == 1 and not visited[next_r][next_c]:
                    queue.append((next_r, next_c, cur_len + 1))
                    visited[next_r][next_c] = True
    
    return result_len

# grid = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
grid = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
# grid = [[0,0,0], [1,1,0], [1,1,0]] 

print(solution(grid))