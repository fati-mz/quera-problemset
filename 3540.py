### Problem Statement
# Mehdi wants to play a childhood game called "Walnut, I broke it" but he has modified the rules to play alone. He stands `n` centimeters away from a wall and wants to reach the wall. He can take steps either longitudinally (lengthwise) or transversely (widthwise). We need to determine how many longitudinal and transverse steps he should take to exactly reach the wall, or determine if it’s impossible.

### Input
# - The first line contains three integers `n`, `x`, and `y`:
#   - `n` is the distance to the wall.
#   - `x` is the step length in the longitudinal direction.
#   - `y` is the step length in the transverse direction.

# Constraints:
# - \(1 \leq n, x, y \leq 100,000\)

### Output
# - If it’s possible to reach exactly `n` centimeters using any combination of steps, print two integers: the number of longitudinal and transverse steps.
# - If it’s not possible, print `-1`.

### Example
# - Input: `10 2 3`
#   - Output: `2 2` or `0 5`
# - Input: `10 4 7`
#   - Output: `-1`

### Explanation
# To solve this problem, we need to find non-negative integers `a` and `b` such that:
# \[ n = a \times x + b \times y \]

# Here’s the step-by-step approach:

# 1. **Iterate through possible values of `a`**:
#    - For each value of `a` from `0` to `n // x` (maximum possible longitudinal steps that fit within `n`), calculate the remaining distance to cover using transverse steps.
#    - Check if the remaining distance is perfectly divisible by `y` (i.e., it can be covered by transverse steps without any remainder).
#    - If divisible, calculate `b` and return the pair `(a, b)`.

# 2. **Edge Case**:
#    - If no combination of steps `(a, b)` satisfies the condition, return `-1`.

### Python Implementation

def find_steps(n, x, y):
    for a in range(n // x + 1):
        if (n - a * x) % y == 0:
            b = (n - a * x) // y
            return a, b
    return -1

# دریافت ورودی
n, x, y = map(int, input().split())

result = find_steps(n, x, y)

if result == -1:
    print(-1)
else:
    print(result[0], result[1])

### Detailed Explanation of the Code
# 1. **Function Definition**:
#    - `find_steps(n, x, y)`:
#      - This function iterates over possible values of `a` (longitudinal steps).
#      - For each `a`, it checks if the remaining distance `n - a * x` is divisible by `y`.
#      - If divisible, it calculates `b` (transverse steps) and returns the pair `(a, b)`.
#      - If no valid pair is found, it returns `-1`.

# 2. **Reading Input**:
#    - The input values are read and split into `n`, `x`, and `y`.

# 3. **Finding Steps**:
#    - The function is called with the input values to find the number of steps.

# 4. **Output**:
#    - If the function returns `-1`, it prints `-1`.
#    - Otherwise, it prints the pair of steps `(a, b)`.

# With this approach, we ensure that we check all possible combinations of steps and determine if it’s possible to reach exactly `n` centimeters. If not, we correctly return `-1`.
