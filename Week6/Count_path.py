def countPath(num):

    len_x = len(num)
    len_y = len(num[0])
    dp = [[0 for _ in range(len_x)] for _ in range(len_y)]
    for i in range(len_x):
        if num[0][i] != 1:
            dp[0][i] = 1
        else:
            dp[0][i] = 0

    for i in range(len_y):
        if num[i][0] != 1:
            dp[i][0] = 1
        else:
            dp[i][0] = 0
    for i in range(1, len_x):
        for j in range(1, len_y):
            if num[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[len_x - 1][len_y - 1]

num = [[0,0,0],[0,1,0],[0,0,0]]
print(countPath(num))