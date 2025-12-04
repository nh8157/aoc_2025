def accessible_by_forklift(grid, x, y):
    count = 0
    if grid[x][y] == ".":
        return 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if i + x  >= 0 and i + x < len(grid) and y + j >= 0 and y + j < len(grid[0]) and grid[i + x][y + j] == "@":
                count += 1
    return 1 if count < 4 else 1

def total_accessible(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            total += accessible_by_forklift(grid, i, j)
    return total

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [line.strip("\n") for line in f.readlines()]
        print(total_accessible(lines))
