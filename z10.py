def check_zeros(tab):
    n = len(tab)
    zeros_cols = [False for _ in range(n)]
    for row in range(n):
        zero_in_row = False
        for col in range(n):
            if tab[row][col] == 0:
                zeros_cols[col] = True
                zero_in_row = True
        if not zero_in_row:
            return False
    for e in range(n):
        if not zeros_cols[e]:
            return False
    return True


tab = [[3, 6, 0],
       [0, 3, 4],
       [0, 0, 8]]

print(check_zeros(tab))