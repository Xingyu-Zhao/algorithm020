#a + b = -c (target) target 有很多
#1. 暴力求解 三重循环O(N^2）
def threesum1(num):
    result = []
    num.sort()
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            for k in range(j+1, len(num)):
                if num[i] + num[j] == -num[k]:
                    r = tuple([num[i], num[j], num[k]])
                    result.append(r)
    return set(result)


# 2. hash，两重暴力
#3. 夹逼
def threesum2(num):
    num.sort()
    result = []
    for i in range(len(num)-2):
        j = i +1
        k = len(num) -1
        while j != k:
            if num[i] + num[j] + num[k] <0:
                j += 1

            elif num[i] + num[j] + num[k] >0:
                k -=1

            else:
                r = tuple([num[i], num[j], num[k]])
                result.append(r)
                break
    return set(result)


num = [-1, 0, 1, 2, -1, -4]
print(threesum2(num))