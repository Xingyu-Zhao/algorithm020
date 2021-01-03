import collections

class Trie(object):
    def __init__(self):
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char in prefix:
                return False
            node = node[char]
        return True

#1.words遍历 --> board找 O(N*m*m*4^k)
#trie做法
#1. 所有的words,全部放到一个trie里面去，构建起一个字典树
#2. board,进行DFS,dfs产生的每个字符串都在trie里面查找，如果是他的子串且存在，就输出，否则不输出
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
END_OF_WORD = "#"

def dfs(board, i, j, cur_word, cur_dict):
    cur_word += board[i][j]
    cur_dict = cur_dict[board[i][j]]
    if END_OF_WORD in cur_dict:
        result.add(cur_word)
    tmp, board[i][j] = board[i][j], "@"
    for k in range(4):
        x, y = i + dx[k] + dy[k]
        if 0 <= x < m and 0 <= y < self.n\
            and board[x][y] != '@' and board[x][y] in cur_dict:
            dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp


class solution:
    def _dfs(self, board, i, j, cur_word, cur_dict):
        ###递归的终止条件
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if END_OF_WORD in cur_dict:
            self.result.add(cur_word)
        ###
        ###当前逻辑的处理
        tmp, board[i][j] = board[i][j], '@'
        for k in range(4):
            x, y = i + dx[k], j+ dy[k]
        ###下探到下一层
            if 0 <= x < self.m and 0 <= y < self.n \
                    and board[x][y] != '@' and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)
        ##恢复之前的层的状态
            board[i][j] = tmp

    def findwords(self, board, words):
        if not board or not board[0] : return []
        if not words: return []
        self.result = set()

        #构建trie,且把单词插入进去
        root = collections.defaultdict()
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, collections.defaultdict())
            node[END_OF_WORD] = END_OF_WORD
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)
        return list(self.result)

words = ["oath", "pea", "eat", "rain"]
board = [['o', 'a', 'a', 'n'],
         ['e', 't', 'a', 'e'],
         ['i', 'h', 'k', 'r'],
         ['i', 'f', 'l', 'v']]

aa = solution()
result = aa.findwords(board = board, words= words)
print(result)
