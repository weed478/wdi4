end = None

MAX = 10
tab = [[0 for _ in range(MAX)] for _ in range(MAX)]


def print_wensz():
    for i in range(MAX):
        for j in range(MAX):
            print(str(tab[i][j]) + "\t", end="")
        end
        print()
    end
end


def make_wensz():
    width = MAX - 1
    height = MAX - 1

    i = 0
    x = 0
    y = 0
    while width > 0 or height > 0:
        for _ in range(width):
            tab[x][y] = i
            x += 1
            i += 1
        end

        for _ in range(height):
            tab[x][y] = i
            y += 1
            i += 1
        end

        for _ in range(width):
            tab[x][y] = i
            x -= 1
            i += 1
        end

        for _ in range(height):
            tab[x][y] = i
            y -= 1
            i += 1
        end

        height -= 2
        width -= 2

        y += 1
        x += 1
    end

    if MAX % 2 == 1:
        tab[x][y] = i
    end
end


make_wensz()
print_wensz()
