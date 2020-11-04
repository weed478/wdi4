tab = [[2, 8, 24, 42, 14], [7, 8, 15, 3, 5], [3, 8, 7, 1, 6], [3, 5, 7, 9, 1], [1, 7, 5, 3, 332]]
tabBe = [[91, 18, 24, 42, 2], [7, 8, 15, 3, 5], [3, 8, 7, 1, 6], [3, 5, 7, 9, 1], [1, 7, 5, 3, 332]]


def has_even(num):
    while num > 0:
        num, digit = divmod(num, 10)
        if digit % 2 == 0:
            return True
    return False


def hehe(tab):
    for row in tab:
        all_even = True
        for n in row:
            if not has_even(n):
                all_even = False
                break

        if all_even:
            return True

    return False


print(hehe(tab))
print(hehe(tabBe))
