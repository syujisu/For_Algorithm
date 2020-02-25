# 문제
# 1부터 N까지의 수를 오름차순으로 쓴 수열 1 2 3 ... N을 생각하자.
# 그리고 '+'나 '-', 또는 ' '(공백)을 숫자 사이에 삽입하자(+는 더하기, -는 빼기, 공백은 숫자를 이어 붙이는 것을 뜻한다). 이렇게 만든 수식의 값을 계산하고 그 결과가 0이 될 수 있는지를 살피자.
# N이 주어졌을 때 수식의 결과가 0이 되는 모든 수식을 찾는 프로그램을 작성하라.

# 입력
# 첫 번째 줄에 테스트 케이스의 개수가 주어진다(<10).
# 각 테스트 케이스엔 자연수 N이 주어진다(3 <= N <= 9).

# 출력
# 각 테스트 케이스에 대해 ASCII 순서에 따라 결과가 0이 되는 모든 수식을 출력한다. 각 테스트 케이스의 결과는 한 줄을 띄워 구분한다.

# 예제 입력 1 
# 2 3 7

# 예제 출력 1 
# 1+2-3
# 1+2-3+4-5-6+7
# 1+2-3-4+5+6-7
# 1-2 3+4+5+6+7
# 1-2 3-4 5+6 7
# 1-2+3+4-5+6-7
# 1-2-3-4-5+6+7

import copy
def recursive(array, n):
    if len(array) == n:
        operators_list.append(copy.deepcopy(array)) #깊은 복사 ; 테스트 케이스마다 다른 형식을 보여줘야 하니까
        return
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

test_case = int(input())

for _ in range(test_case):
    operators_list = []
    n = int(input())
    recursive([], n - 1)

    integers = [i for i in range(1, n + 1)]

    for operators in operators_list:
        string = ""
        for i in range(n - 1):
            string += str(integers[i]) + operators[i]
        string += str(integers[-1])
        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()