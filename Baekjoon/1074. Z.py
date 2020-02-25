# 문제
# 한수는 2차원 배열 (항상 2^N * 2^N 크기이다)을 Z모양으로 탐색하려고 한다. 예를 들어, 2*2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.
# 만약, 2차원 배열의 크기가 2^N * 2^N라서 왼쪽 위에 있는 칸이 하나가 아니라면, 배열을 4등분 한 후에 (크기가 같은 2^(N-1)로) 재귀적으로 순서대로 방문한다.
# N이 주어졌을 때, (r, c)를 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N r c가 주어진다. N은 15보다 작거나 같은 자연수이고, r과 c는 0보다 크거나 같고, 2^N-1보다 작거나 같은 정수이다
# 출력
# 첫째 줄에 문제의 정답을 출력한다.

# 예제 입력 1
# 2 3 1

# 예제 출력 1
# 11

# 예제 입력 2
# 3 7 7

# 예제 출력 2
# 63

n, x, y = map(int, input().split())

def power2(k): # 두배 만드는 함수
    return 1 << k

def go(n, x, y):
    if n == 1:
        return 2*x+y
    else:
        if x < power2(n-1): # 점점 쪼개진다.
            if y < power2(n-1):# 점점 쪼개진다.
                return go(n-1, x, y)
            else:
                return go(n-1, x, y-power2(n-1)) + power2(2*n-2)
        else:
            if y < power2(n-1):
                return go(n-1, x-power2(n-1), y) + power2(2*n-2)*2
            else:
                return go(n-1, x-power2(n-1), y-power2(n-1)) + power2(2*n-2)*3;

print(go(n,x,y))


#or
def Z(n,x,y):
    if n==1:return 0
    if r<x+n//2:
        if c<y+n//2:
            return Z(n//2,x,y) #0분면
        else:
            return Z(n//2,x,y+n//2)+n*n//4 #1분면
    else:
        if c<y+n//2:
            return Z(n//2,x+n//2,y)+n*n//4*2 #2분면
        else:
            return Z(n//2,x+n//2,y+n//2)+n*n//4*3 #3분면
n,r,c=map(int,input().split())
print(Z(2**n,0,0))