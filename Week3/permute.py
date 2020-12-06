from typing import List


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         def dfs(nums, size, depth, path, used, res):
#             if depth == size:
#                 res.append(path[:])
#                 return
#
#             for i in range(size):
#                 if not used[i]:
#                     used[i] = True
#                     path.append(nums[i])
#
#                     dfs(nums, size, depth + 1, path, used, res)
#
#                     used[i] = False
#                     path.pop()
#
#         size = len(nums)
#         if len(nums) == 0:
#             return []
#
#         used = [False for _ in range(size)]
#         res = []
#         dfs(nums, size, 0, [], used, res)
#         return res
import copy

class Solution1:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        res = []
        backtrack()
        return res


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False for _ in range(len(nums))]
        def dfs(nums, visited, path, depth, res):
            if depth == len(nums):
                res.append(copy.deepcopy(path))
                return
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    dfs(nums, visited, path, depth+1, res)
                    visited[i] = False
                    path.pop()
        path = []
        depth = 0
        res = []
        dfs(nums, visited, path, depth, res)
        return res










if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution2()
    res = solution.permute(nums)
    print(res)
