# 과제 24

a = list(map(int, input().split(";")))
a.sort(reverse = True)
for i in a:
  print(f"{i:>9}")
