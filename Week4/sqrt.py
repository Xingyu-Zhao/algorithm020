#二分查找， y = x^2, (x>0), 是抛物线，在y轴右侧单调递增，有上下界
def mysqrt(x):
    if x == 1 or x == 0:
        return x
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
    return right

#newton
def mysqrt2(x):
    if x == 0:
        return x
    cur = 1
    while True:
        pre = cur
        cur = (cur + x / cur) /2
        if abs(cur - pre) < 1e-6:
            return cur




print(mysqrt2(9))