class Solution(object):
    def combine(self, n, k):
        if k > n or k == 0:
            return []
        if k == 1:
            return [[i] for i in range(1, n + 1)]
        if k == n:
            return [[i for i in range(1, n + 1)]]

        answer = self.combine(n - 1, k)
        for item in self.combine(n - 1, k - 1):
            item.append(n)
            answer.append(item)

        return answer

s = Solution()
print(s.combine(n = 4, k = 2))