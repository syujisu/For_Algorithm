positions = []

for _ in range(int(input())):
    positions.append(list(map(int, input().split())))

positions.sort(key=lambda x: (x[1], x[0]))

print('\n'.join([' '.join(list(map(str, position)))
                 for position in positions]))