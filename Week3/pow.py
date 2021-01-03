#暴力循环，O(N)
def my_pow(x, n):
    result = x
    for i in range(n-1):
        result = result * x
    return result

#分治--就是递归的思想
#template 1.terminator 2. process (split your big problem ), 3. drill down(subproblem)
#,merge(subresult)4. reverse states

#subproblem --> pow(x, n/2), 时间复杂度就是log(N), 如果n = 1024的话，只需要需要10次循环
#因为每次2^10 = 1024

def my_pow1(x, n):
    #1.terminator
    if n == 0:
        return 1.0
    #2. process (split your big problem )
    y = my_pow1(x, n // 2)
    #drill down(subproblem)
    if n % 2 == 0:
        result = y * y
    else:
        result = y * y * x
    return result


if __name__ == '__main__':
    print(my_pow1(2, 7))