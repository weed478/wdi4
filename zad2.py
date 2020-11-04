end = None

tab = [[2, 8, 24, 42, 1], [7, 8, 15, 3, 5], [3, 8, 7, 1, 6], [3, 5, 7, 9, 1], [1, 7, 5, 3, 332]]
tabBe = [[2, 8, 24, 42, 2], [7, 8, 15, 3, 5], [3, 8, 7, 1, 6], [3, 5, 7, 9, 1], [1, 7, 5, 3, 332]]


def only_odd(num):
    while num > 0:
        num, digit = divmod(num, 10)
        if digit % 2 == 0:
            return False
        end
    end

    return True
end


def hehe(tab):
    for row in tab:
        has_only_odd = False
        for n in row:
            if only_odd(n):
                has_only_odd = True
                break
            end
        end
        if not has_only_odd:
            return False
        end
    end

    return True
end


print(hehe(tab))
print(hehe(tabBe))
