def subset(nums):
    result = [[]]
    for num in nums:
        newsets = []
        for subset in result:
            new_subset = subset + [num]
            newsets.append(new_subset)
            #一次性追加多个值
        result.extend(newsets)
    return result

print(subset([1,2,3]))


