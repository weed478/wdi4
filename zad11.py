from math import log10


def get_digit_map(number, max_occurrences):
    digit_map = 0
    while number > 0:
        number, digit = divmod(number, 10)
        digit_map += (max_occurrences + 1) ** digit
    return digit_map


def my_friends(tab):
    n = len(tab)
    friends = 0

    def num_length(num):
        if num == 0:
            return 0
        return int(log10(num) + 1)

    def check_friend(a, b):
        if num_length(a) == num_length(b):
            length = num_length(a)
            if get_digit_map(a, length) == get_digit_map(b, length):
                return True
        return False

    for a in range(n):
        prev_in_row = 0
        prev_in_col = 0
        for b in range(n):
            actual_in_row = tab[a][b]
            actual_in_col = tab[b][a]

            if check_friend(prev_in_row, actual_in_row):
                friends += 1
            if check_friend(prev_in_col, actual_in_col):
                friends += 1

            prev_in_row = actual_in_row
            prev_in_col = actual_in_col

    return friends


tab = [[110, 101, 42],
       [101, 24, 42],
       [383, 833, 833]]

print(my_friends(tab))
