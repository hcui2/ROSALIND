with open("TestData/rosalind_ba5b.txt") as f:
    first = next(f)
    n, m = first.strip().split()
    n, m = int(n), int(m)

    lines = f.readlines()
    lines = [l.strip() for l in lines]
    sep_idx = lines.index('-')
    vertical = lines[:sep_idx]
    horizontal = lines[sep_idx+1:]
    vertical = [[int(w) for w in l.split()] for l in vertical]
    horizontal = [[int(w) for w in l.split()] for l in horizontal]

# n is the row number; m is the column number.
def longest_path(vertical_weights, horizontal_weights, n, m ):

    dp = [[0] * (m+1) for i in range(n+1)]
    # fill the first column and first row
    for i in range(n):
        dp[i+1][0] = vertical[i][0] + dp[i][0]
    for j in range(m):
        dp[0][j+1] = horizontal[0][j] + dp[0][j]

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = max(dp[i-1][j] + vertical[i-1][j], dp[i][j-1] + horizontal[i][j-1])
    return dp[-1][-1]

res = longest_path(vertical, horizontal, n, m)
print(res)
