# 과제 16

a = list(map(int, input().split()))
min_value = min(a)
max_value = max(a)

result = sum(a)

print(result - min_value + max_value)
