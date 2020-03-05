# 문제
# N×M크기의 배열로 표현되는 미로가 있다.

# 1	0	1	1	1	1
# 1	0	1	0	1	0
# 1	0	1	0	1	1
# 1	1	1	0	1	1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.


#BFS로 미로 탈출 알고리즘 정의
def bfs(maze, i, j, N, M):
    visited = [] #방문한 노드
    queue = [[i, j]] #BFS로 사용될 큐
    distance = [[0 for _ in range(M)] for _ in range(N)] #해당 지점까지의 거리를 담는 리스트
    distance[0][0] = 1 #첫 시작은 1
    
    while queue: 
        [i, j] = queue.pop(0) #BFS 큐에 넣어줌
        visited.append([i, j]) #방문 리스트에 쌓아줌
        
        #상하좌우 탐색
        if i < N-1 and maze[i+1][j] == 1 and [i+1, j] not in visited and [i+1, j] not in queue:
            queue.append([i+1, j])
            distance[i+1][j] = distance[i][j] + 1
        if j < M-1 and maze[i][j+1] == 1 and [i, j+1] not in visited and [i, j+1] not in queue:
            queue.append([i, j+1])
            distance[i][j+1] = distance[i][j] + 1
        if j > 0 and maze[i][j-1] == 1 and [i, j-1] not in visited and [i, j-1] not in queue:
            queue.append([i, j-1])
            distance[i][j-1] = distance[i][j] + 1
        if i > 0 and maze[i-1][j] == 1 and [i-1, j] not in visited and [i-1, j] not in queue:
            queue.append([i-1, j])
            distance[i-1][j] = distance[i][j] + 1
            
    return distance[N-1][M-1] #마지막 도착지의 거리를 반환