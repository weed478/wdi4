tab = [[2, 3, 3, 7, 9],
       [3, 4, 7, 7, 12],
       [9, 9, 12, 13, 16],
       [2, 4, 7, 12, 13],
       [1, 2, 7, 7, 9]]


def convert_tab(tab):
    n = len(tab)
    n_col = [0 for _ in range(n)]
    tab_out = []

    point = 0
    changed_point = False
    while not changed_point:
        for row in range(n):
            if n_col[row] < n:
                if tab[row][n_col[row]] <= tab[point][n_col[point]]:
                    changed_point = True
                    point = row

        if changed_point:
            tab_out.append(tab[point][n_col[point]])
            n_col[point] += 1
            changed_point = False

            for row in range(n):
                if n_col[row] < n:
                    point = row
                    break
                if row == n - 1:
                    changed_point = True
    return tab_out


print(convert_tab(tab))
