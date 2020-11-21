#1枚举，复杂度O(N^2)

def maxArea_enumeric(num):
    max_a = 0
    for i in range(len(num)):
        #不用再遍历自己了
        for j in range(i+1, len(num)):
            area = (j - i) *min(num[i], num[j])
            max_a = max(max_a, area)
    return max_a

#2选择最左边和最右边的棒子（宽度最宽），然后慢慢往里收敛。只选择高度比外边棒子高的O（N）,左右夹逼

def maxArea_quick(num):
    area_max = 0
    j = len(num) - 1
    i = 0
    while i < len(num):
        area = (j - i) * min(num[i], num[j])
        if num[i] > num[j]:
            j -= 1
        else:
            i += 1
        area_max = max(area, area_max)

        if i == j:
            break

    return area_max

num = [1,8,6,2,5,4,8,3,7]

# print(bb)
# print(maxArea_enumeric(num))
print(maxArea_quick(num))