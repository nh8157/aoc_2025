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
    return count < 4

def total_accessible(grid):
    count = 0
    coords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if accessible_by_forklift(grid, i, j):
                count += 1
                coords.append([i, j])

    if count == 0:
        return 0

    for coord in coords:
        grid[coord[0]][coord[1]] = "."

    return count + total_accessible(grid)

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = [list(line.strip("\n")) for line in f.readlines()]
        print(lines)
        print(total_accessible(lines))
