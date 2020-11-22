#遍历循环,复杂度O(N), 但是要重新开辟数组,空间复杂度O(N)
def rotate(num, k):
    res = num.copy()
    for i in range(len(num)):
        j = (i + k) % (len(num))
        res[j] = num[i]
    return res

#无需重新开辟数组，把被替换的数字直接用temp表示,空间复杂度O(1)
def rotate1(num, k):
    count = 0
    k = k % len(num)
    start = 0
    cur = start
    pre = num[cur]
    while count < len(num):
        next = (cur + k) % len(num)
        temp = num[next]
        num[next] = pre
        pre = temp
        cur = next
        count += 1

    return num



print(rotate1([1,2,3,4,5,6,7], k=3))

