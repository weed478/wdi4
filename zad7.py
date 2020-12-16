tab = [[2,  3,  3,  7,  9],
       [3,  4,  7,  7,  12],
       [9,  9,  12, 13, 16],
       [2,  4,  7,  12, 13],
       [1,  2,  7,  7,  9]]


def convert_tab(tab):
    n = len(tab)
    n_col = [0 for _ in range(n)]
    tab_out = []

    smallest_in_row = 0
    changed_in_row = False
    while not changed_in_row:
        for row in range(n):
            if n_col[row] < n:
                if tab[row][n_col[row]] <= tab[smallest_in_row][n_col[smallest_in_row]]:
                    changed_in_row = True
                    smallest_in_row = row

        if changed_in_row:
            tab_out.append(tab[smallest_in_row][n_col[smallest_in_row]])
            n_col[smallest_in_row] += 1
            changed_in_row = False

            for row in range(n):
                if n_col[row] < n:
                    smallest_in_row = row
                    break
                if row == n - 1:
                    changed_in_row = True
    return tab_out


print(convert_tab(tab))
