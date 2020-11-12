def find_best(tab):
    N = len(tab)
    max_sum = 0
    best_p = (None, None)

    for y in range(N):
        for x in range(N):
            s = 0

            if y - 1 >= 0:
                if x - 1 >= 0:
                    s += tab[y - 1][x - 1]

                s += tab[y - 1][x]

                if x + 1 < N:
                    s += tab[y - 1][x + 1]

            if x - 1 >= 0:
                s += tab[y][x - 1]

            if x + 1 < N:
                s += tab[y][x + 1]

            if y + 1 < N:
                if x - 1 >= 0:
                    s += tab[y + 1][x - 1]

                s += tab[y + 1][x]

                if x + 1 < N:
                    s += tab[y + 1][x + 1]

            if s > max_sum:
                max_sum = s
                best_p = (x, y)

    return best_p


tab = [[0, 0, 0, 0, 0],
       [100, 1, 1, 0, 0],
       [1, 0, 5, 5, 5],
       [1, 1, 5, 0, 5],
       [0, 0, 5, 5, 5]]

print(find_best(tab))
