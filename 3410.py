a=int(input())

def pascal_triangle(n, memo={}):
    if n == 0:
        return [1]
    elif n in memo:
        return memo[n]
    else:
        row = [1]
        prev_row = pascal_triangle(n-1, memo)
        for i in range(1, n):
            row.append(prev_row[i-1] + prev_row[i])
        row.append(1)
        memo[n] = row
        return row

for i in range(a):
    row = pascal_triangle(i)
    print(*row)
