class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def NeighborExist(board,word,i,j,path):
            if len(word) == 0:
                return True

            if i - 1 >= 0 and word[0] == board[i-1][j] and [i-1,j] not in path:
                if NeighborExist(board,word[1:],i-1,j, path + [[i-1,j]]):
                    return True

            if i + 1 < len(board) and word[0] == board[i+1][j] and [i+1,j] not in path:
                if NeighborExist(board,word[1:],i+1,j, path + [[i+1,j]]):
                    return True

            if j + 1 < len(board[0]) and word[0] == board[i][j+1] and [i,j+1] not in path:
                if NeighborExist(board,word[1:],i,j+1, path + [[i,j+1]]):
                    return True

            if j - 1 >= 0 and word[0] == board[i][j-1] and [i,j-1] not in path:
                if NeighborExist(board,word[1:],i,j-1, path + [[i,j-1]]):
                    return True

        path = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if word[0] == board[i][j]:
                    if NeighborExist(board,word[1:],i,j,path + [[i,j]]):
                        return True
        return False



board = [["a","a","a","a"],
         ["a","a","a","a"],
         ["a","a","a","a"],
         ["a","a","a","a"],
         ["a","a","a","b"]]
word = "aaaaaaaaaaaaaaaaaaaa"
"""
board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
"""
p = Solution()
print(p.exist(board,word))


