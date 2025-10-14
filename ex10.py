# 과제 20

a, b = map(int, input().split())

first = []

for i in range(a, b + 1):
    first.append(2 ** i)

if len(first) > 3:
    first.pop(1)
    first.pop(-2)
elif len(first) == 3:
    first.pop(1)

print(first) 
