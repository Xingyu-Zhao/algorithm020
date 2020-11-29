#暴力排序，时间复杂度O(nlog(n))
import heapq
def getLeastNumbers(nums, k):
    #sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
    # list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
    num = sorted(nums)
    return num[:k]

#堆的思想，时间复杂度O(nlogk)
def getLeastNumbers_1(arr, k):
    if k == 0:
        return list()

    hp = [-x for x in arr[:k]]
    #将一个列表转换为堆，实现小顶堆,时间复杂度为O(1)
    heapq.heapify(hp)
    for i in range(k, len(arr)):
        if -hp[0] > arr[i]:
            #heapq.heappop弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，抛出 IndexError
            #弹出堆顶元素 时间复杂度为O(logk)
            heapq.heappop(hp)
            #:将x压入堆中 时间复杂度为O(logk)
            heapq.heappush(hp, -arr[i])
    ans = [-x for x in hp]
    return ans


arr = [3,2,14,5,6,1]
k = 2
print(getLeastNumbers_1(arr, k))