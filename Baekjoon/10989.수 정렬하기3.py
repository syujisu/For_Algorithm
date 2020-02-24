# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1 복사
# 10 5 2 3 1 4 2 3 5 1 7

# 예제 출력 1 복사
# 1 1 2 2 3 3 4 5 5 7

import sys

case = int(input())
result = [0 for i in range(10001)]
#10,000 이 들어갈 수 있는 리스트 만들어 하나씩 더해주고 메모리에서 없앰
for num in sys.stdin:
    result[int(num)] += 1

for i in range(10001):
    if result[i] > 0:
        for j in range(result[i]):
            print(i)