n = int(input())
c = 2
for row in range(1, n + 1):
    for i in range(1, c):
        if i <= row:
            print(i, end='')
        else:
            print(2*row - i, end='')
    c = c + 2
    print()
