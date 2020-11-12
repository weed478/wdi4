def sum_row(t, y):
    return sum(t[y])


def sum_col(t, x):
    return sum([row[x] for row in t])


def place_pieces(board):
    N = len(board)
    row_sums = [sum_row(tab, row) for row in range(N)]
    col_sums = [sum_col(tab, col) for col in range(N)]

    max_sum = 0
    best_p1 = (None, None)
    best_p2 = (None, None)

    for i1 in range(N*N - 1):
        for i2 in range(i1 + 1, N*N):
            y1, x1 = divmod(i1, N)
            y2, x2 = divmod(i2, N)

            s = row_sums[y1] + col_sums[x1] - board[y1][x2] - board[y2][x1] - board[y1][x1] - board[y2][x2]

            if x1 != x2 and y1 != y2:
                s -= board[y1][x1] + board[y2][x2]

            if x1 != x2:
                s += col_sums[x2]

            if y1 != y2:
                s += row_sums[y2]

            if s > max_sum:
                max_sum = s
                best_p1 = (x1, y1)
                best_p2 = (x2, y2)

        # end for i2
    # end for i1

    return best_p1, best_p2


"""
   x -->
y
|
V
"""

#       0  1  2  3  4  5  6  7
tab = [[1, 2, 3, 4, 5, 6, 7, 8],  # 0
       [2, 0, 0, 0, 5, 0, 0, 0],  # 1
       [3, 0, 0, 0, 5, 0, 0, 0],  # 2
       [4, 4, 4, 4, 5, 4, 4, 4],  # 3
       [5, 0, 0, 0, 5, 0, 0, 0],  # 4
       [6, 2, 0, 0, 5, 0, 1, 0],  # 5
       [7, 0, 3, 0, 5, 7, 2, 0],  # 6
       [8, 0, 0, 0, 5, 0, 0, 0]]  # 7

print(place_pieces(tab))
