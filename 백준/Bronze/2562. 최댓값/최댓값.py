import sys
num = []
for i in range(9):
    num.append(int(sys.stdin.readline().strip()))

print(max(num))
print(num.index(max(num)) + 1)