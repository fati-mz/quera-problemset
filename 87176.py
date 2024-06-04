def game(number):
    n = [int(digit) for digit in str(number)]
    return max(n)-min(n)
