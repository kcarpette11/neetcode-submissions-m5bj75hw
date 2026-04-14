class Solution:
   
    def findWords(self, board, words):
        rows, cols = len(board), len(board[0])
        res = set()

        # -------- build trie --------
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node["$"] = word   # end marker storing full word

        # -------- dfs search --------
        def dfs(r, c, node):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            char = board[r][c]
            if char not in node:
                return

            nxt = node[char]

            # found a word
            if "$" in nxt:
                res.add(nxt["$"])

            board[r][c] = "#"

            dfs(r+1, c, nxt)
            dfs(r-1, c, nxt)
            dfs(r, c+1, nxt)
            dfs(r, c-1, nxt)

            board[r][c] = char

        # -------- start search --------
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return list(res)



       



        