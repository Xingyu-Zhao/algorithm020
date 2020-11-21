#空间换时间，升维
#暴力
#基本情况，枚举你n=1, n=2, n=3,数学归纳法
#找重复的子问题， （if else; for while; recursion）

#就是一个只能从n-1走过来或者n-2台阶走过来，所以f(n) = f(n-1) + f(n-2)：Fibonacci

#1.递归O(2^n)
def climbStairs(n):
    if n <3 :
        return n

    else:
        return climbStairs(n-1) + climbStairs(n-2)


#2 就保存三个值，然后不断累加和覆盖, O(N)
def climbStairs2(n):
    if n < 3:
        return n
    f1, f2, f3 = 1, 2, 3
    for i in range (3, n+1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    return f3

ccc = climbStairs2(4)
ddd = climbStairs(4)
print(ddd)