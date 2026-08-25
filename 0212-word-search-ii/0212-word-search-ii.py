from typing import List

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Build Trie
        trie = {}

        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node["#"] = word

        result = []
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node:
                return

            next_node = node[ch]

            # Complete word found
            if "#" in next_node:
                result.append(next_node["#"])
                del next_node["#"]

            # Mark visited
            board[r][c] = "#"

            # Up
            if r > 0 and board[r - 1][c] != "#":
                dfs(r - 1, c, next_node)

            # Down
            if r < rows - 1 and board[r + 1][c] != "#":
                dfs(r + 1, c, next_node)

            # Left
            if c > 0 and board[r][c - 1] != "#":
                dfs(r, c - 1, next_node)

            # Right
            if c < cols - 1 and board[r][c + 1] != "#":
                dfs(r, c + 1, next_node)

            # Backtrack
            board[r][c] = ch

            # Trie pruning
            if not next_node:
                del node[ch]

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, trie)

        return result