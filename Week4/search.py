#二分查找
def search(nums, target):
    if not nums:
        return -1
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[0] <= nums[mid]:
            if nums[0] <= target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target <= nums[len(nums) - 1]:
                low = mid + 1
            else:
                high = mid - 1
    return -1

print(search(nums = [4,5,6,7,0,1,2], target=2))