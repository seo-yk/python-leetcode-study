class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coord(x, n):
            index = x-1
            r = (n-1) - (index // n)

            if (index // n) % 2 == 0:
                c = index % n
            else:
                c = (n-1) - (index % n)

            return r, c

        visited = set([1])
        queue = deque([(1, 0)])

        def bfs():
            while queue:
                cur, moves = queue.popleft()

                for i in range(1, 7):
                    next_square = cur + i

                    if next_square > n * n:
                        continue

                    r, c = get_coord(next_square, n)

                    destination = board[r][c] if board[r][c] != -1 else next_square

                    if destination == n * n:
                        return moves + 1

                    if destination not in visited:
                        visited.add(destination)
                        queue.append((destination, moves + 1))
                        
            return -1

        return bfs()