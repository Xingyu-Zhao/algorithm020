def age(n):
    if n == 1:
        return 18
    else:
        return age(n - 1) +2
#
# print(age(4))
# print([1] + [2])
# print()

cols = []
for col in range(8):  # 遍历列
    # 判断当前的皇后是否已经与之前皇后的位置冲突
    # p = col < 3 or col > 6
    # if col in self.cols or row + col in self.pie or row - col in self.na:
    if col < 3 or col > 6:
        # print(col)
        # go die
        continue

    # update flags
    cols.append(col)

print(cols)