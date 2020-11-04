def sum_row(tab, row):
    sum = 0
    for n in tab[row]:
        sum += n

    return sum


def sum_col(tab, col):
    sum = 0
    for row in range(len(tab)):
        sum += tab[row][col]

    return sum


tab = [[0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0],
       [0, 0, 3, 0, 0],
       [0, 0, 2, 3, 0],
       [0, 0, 0, 0, 0]]


col_sums = [sum_col(tab, col) for col in range(len(tab[0]))]


def smierc(tab):
    max_value = None
    max_row = 0
    max_col = 0

    for row in range(len(tab)):
        row_sum = sum_row(tab, row)
        if row_sum == 0:
            continue

        for col in range(len(tab[0])):
            col_sum = col_sums[col]
            value = col_sum / row_sum
            if max_value is None or value > max_value:
                max_value = value
                max_row = row
                max_col = col

    if max_value is None:
        return None, None
    else:
        return max_row, max_col


print(smierc(tab))


