week=['shanbe','1shanbe','2shanbe','3shanbe','4shanbe','5shanbe','jome']

_ = input()
a = input().split()
_ = input()
a += input().split()
_ = input()
a += input().split()

print(len(set(week).difference(set(a))))