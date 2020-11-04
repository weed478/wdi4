def get_next_row(tab, len_tab):
    next_row = -1
    min_row_value = 0
    for row in range(len(tab)):
        if len_tab[row] < len(tab[0]) and (next_row < 0 or tab[row][len_tab[row]] < min_row_value):
            min_row_value = tab[row][len_tab[row]]
            next_row = row

    return next_row


def zad6(tab_in):
    tab_out = [0] * len(tab_in) ** 2
    out_len = 0
    len_tab = [0] * len(tab_in)

    should_add = True
    prev_value = tab_in[get_next_row(tab_in, len_tab)][0]
    while min(len_tab) < len(tab_in[0]):
        next_row = get_next_row(tab_in, len_tab)
        value = tab_in[next_row][len_tab[next_row]]

        if prev_value != value:
            if should_add:
                tab_out[out_len] = prev_value
                out_len += 1
            should_add = True
        else:
            should_add = False

        prev_value = value
        len_tab[next_row] += 1

    if should_add:
        tab_out[out_len] = prev_value
        out_len += 1

    return tab_out, out_len


tab = [[1, 1, 5, 6, 7],
       [2, 3, 4, 5, 8],
       [5, 8, 8, 10, 12],
       [1, 3, 3, 4, 5]]

out_tab, length = zad6(tab)
print(out_tab[:length])
