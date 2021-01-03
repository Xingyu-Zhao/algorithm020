class Solution(object):
    def solveNQueens(self, n):
        if n < 1: return []
        self.result = []
        #之前皇后所占的列， pie, na
        self.cols = set()
        self.pie = set()
        self.na = set()
        self.DFS(n, 0, [])
        return self._generate_result(n)
    def DFS(self, n, row, cur_state):
        #recursion terminator
        #到了最后一层啦
        if row >= n:
            self.result.append(cur_state)
            return
        #否则对该层进行遍历
        #current level!Do it!
        for col in range(n):#遍历列
            #判断当前的皇后是否已经与之前皇后的位置冲突
            if col in self.cols or row + col in self.pie or row - col in self.na:
                #go die
                continue

            #update flags
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)
            self.DFS(n, row+1, cur_state + [col])
        #reverse states
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def _generate_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append("." * i + "Q" + "." * (n - i - 1))
        return [board[i : i + n] for i in range(0, len(board), n)]

aa = Solution()
print(aa.solveNQueens(4))