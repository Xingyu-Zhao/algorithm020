#1. 暴力,O(N^2)
def twosum_1(num, target):
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            if target == num[i] + num[j]:
                return i,j
            else:
                print("None")

#hashtable,a + b == target --> for each a : check (target - a) exit in the array  (O(N))
def twosum_2(num, target):
    hashtable = dict()
    result = []
    for index, value in enumerate(num):
        #建立一个hashtable，key是list的值, value是对应的index
        #因为最终是返回的index，求啥，啥就为value
        # hashtable[value] = index
        if target-value in hashtable.keys():
            aa = [index, hashtable[target-value]]
            result.append(aa)
        #这句话一定要放在if之后，解决list中有重复值或target-num=num的情况
        #重复值的话，就比如（[3,3], target=6）,在第一个的时候就满足情况，所以直接输出[0,0]
        hashtable[value] = index

    return result


num = [3,3]
target = 6
ans = twosum_2(num, target)
print(ans)