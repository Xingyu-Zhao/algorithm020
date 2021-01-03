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

def jump(nums):
    step = 0
    cur_pos = 0
    if len(nums) == 1:
        return 0
    if nums[0] >= len(nums) -1:
        return 1
    else:
        while cur_pos <= len(nums) - 1:
            if cur_pos + nums[cur_pos] >= len(nums) - 1:
                return step+1
            else:
                next_num = nums[(cur_pos + 1): (cur_pos + nums[cur_pos] + 1)]
                max_index = next_num.index(max(next_num))
                cur_pos = cur_pos + max_index + 1
                step += 1
    return step

def fourSum(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)-3):
        for j in range(i + 1, len(nums)-2):
            k = j + 1
            l = len(nums) - 1
            while k != l:
                if nums[i] + nums[j] + nums[k] + nums[l] < target:
                    k += 1
                elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                    l -= 1
                else:
                    r = tuple([nums[i], nums[j], nums[k], nums[l]])
                    result.append(r)
                    k += 1

    result = list(set(result))
    return result

nums = [-3,-2,-1,0,0,1,2,3]
print(fourSum(nums, 0))
# print(threesum2(nums))
# nums = [1,2,1,1,1]
# print(jump(nums))