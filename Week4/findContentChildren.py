
#贪心算法，时间复杂度：O(nlogn+mlogm)O(nlogn+mlogm)
def findContentChildren(g, s):
    g.sort()
    s.sort()

    i, j = 0, 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1

    return i

print(findContentChildren(g = [1,2,3], s = [1,1]))
print(findContentChildren(g = [1,2], s = [1,2,3]))