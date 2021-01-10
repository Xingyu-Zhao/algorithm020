class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # two get pointers for nums1 and nums2
        p = m + n - 1
        p1 = m -1
        p2 = n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        ###z注意这个
        nums1[:p2 + 1] = nums2[:p2 + 1]
        return nums1




        # p1 = m - 1
        # p2 = n - 1
        # # set pointer for nums1
        # p = m + n - 1
        # # while there are still elements to compare
        # while p1 >= 0 and p2 >= 0:
        #     if nums1[p1] < nums2[p2]:
        #         nums1[p] = nums2[p2]
        #         p2 -= 1
        #     else:
        #         nums1[p] = nums1[p1]
        #         p1 -= 1
        #     p -= 1
        # # add missing elements from nums2
        # nums1[:p2 + 1] = nums2[:p2 + 1]
        # return nums1

nums1 = [ 0]
m = 0
nums2 =[1]
n = 1
solu = Solution()
print(solu.merge(nums1, m, nums2, n))