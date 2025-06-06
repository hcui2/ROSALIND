from typing import *
import sys
sys.setrecursionlimit(10000)

def lcs_backtrack(u, v):
    dp = [[0] * (len(v) + 1) for i in range(len(u) + 1)]
    backtrack_matrix = [[None] * (len(v) + 1) for i in range(len(u) + 1)]

    for i in range(1, len(u)+1):
        for j in range(1, len(v)+1):
            if u[i-1] == v[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            dp[i][j] = max([dp[i-1][j], dp[i][j-1], dp[i][j]])

            # record the path
            if dp[i][j] == dp[i-1][j]:
                backtrack_matrix[i][j] = 'down_vertical'
            elif dp[i][j] == dp[i][j-1]:
                backtrack_matrix[i][j] = 'right_horizontal'
            else:
                backtrack_matrix[i][j] = 'diagonal'

    return backtrack_matrix

def output_lcs(backtrack_matrix, v, i, j, tmp: List):
    if i == 0 or j == 0:
        return
    if backtrack_matrix[i][j] == 'down_vertical':
        output_lcs(backtrack_matrix, v, i-1, j, tmp)
    elif backtrack_matrix[i][j] == 'right_horizontal':
        output_lcs(backtrack_matrix, v, i, j-1, tmp)
    else:
        tmp.insert(0, v[i-1])
        output_lcs(backtrack_matrix, v, i-1, j - 1, tmp)

def lcs_of_strings(u, v):
    matrix = lcs_backtrack(u, v)
    res = []
    output_lcs(matrix, u, len(u), len(v), res)
    return ''.join(res)


with open("TestData/rosalind_ba5c.txt") as f:
    s1 = next(f)
    s2 = next(f)
    lcs = lcs_of_strings(s1.strip(), s2.strip())

print(lcs)

