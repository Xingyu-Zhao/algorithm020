#给定两个字符串s和t， 编写一个函数来判断t是否是s的字母异位词
#1. 面试官沟通意思
#2. 可能的解决方案， -->选出最优的 （时间&空间）
#3. code
#4. test cases

#1. 暴力，直接调用，O(NlogN)
def isAnagram_1(a, b):
    # la = list(a)
    # la.sort()
    la = sorted(a)
    a_sort = "".join(la)
    # lb = list(b)
    # lb.sort()
    lb = sorted(b)
    b_sort = "".join(lb)
    if a_sort == b_sort:
        return True
    else:
        return False

#2.hash, map,统计每个字符的频次， 若频次相同，则是一样的 时间复杂度O(N)
def isAnagram_2(a, b):
    hash_table_a = {}
    hash_table_b = {}

    for char in a:
        if char in hash_table_a:
            hash_table_a[char] += 1
        else:
            hash_table_a[char] = 1
    for char in b:
        if char in hash_table_b:
            hash_table_b[char] += 1
        else:
            hash_table_b[char] = 1
    if hash_table_a == hash_table_b:
        return True
    else:
        return False

def isAnagram_3(a, b):
    hash_table_a = {}
    for char in a:
        if char in hash_table_a:
            hash_table_a[char] += 1
        else:
            hash_table_a[char] = 1
    for char in b:
        if char in hash_table_a:
            hash_table_a[char] -= 1
        else:
            hash_table_a[char] = 1
    for value in hash_table_a.values():
        if value != 0:
            return False
        else:
            return True
    else:
        return False


s = "anagram"
t = "nagaram"
print(isAnagram_3(s,t))

