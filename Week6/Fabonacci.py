#记忆化搜索(自顶向下的解决问题)
MAXSIZE = 1000
memo = [-1 for i in range(MAXSIZE)]
def fib3(n,memo):
    if n <= 0:
        return n
    if memo[n] == -1:
        memo[n] = fib3(n-1,memo) + fib3(n-2,memo)
    return memo[n]
print(fib3(6,memo))

#动态规划(自底向上的解决问题)
def fib2(n):
    memo = [-1 for x in range(n+1)]
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1]+memo[i-2]
    return memo[n]

print(fib2(6))