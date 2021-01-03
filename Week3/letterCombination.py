class generator:
    def __init__(self, n):
        self.max = n
    #加限制条件，left随时可以加，左括号数量大于右括号数量
    def genbrackets(self, left = 0, right = 0,  str = ""):
        # recursion terminator递归的终止条件
        if left == self.max and right == self.max:
            print(str)
            return
    # process logic in current level处理当前层的逻辑
    #     str1 = str + "("
    #     str2 = str + ")"
    #drill down下探到下一层
        if left < self.max:
            generator.genbrackets(self, left = left +1, right=right, str = str + "(")
        if left > right and right < self.max:
            generator.genbrackets(self, left = left, right = right + 1, str = str + ")")
    #reverse the current level status if needed清理当前层
a = generator(n = 3)
print(a.genbrackets())