n, l, q = map(int, input().split())
dataset = {}
for i in range(n):
    s, res = input().split()
    dataset[s] = res
for i in range(l):
    s = input().strip()
    if s in dataset:
        print(dataset[s])
    else:
        print("Unknown")