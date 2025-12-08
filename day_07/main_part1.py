def count_splits(tree):
    prev_level = tree[0]
    count = 0
    for row in range(1, len(tree)):
        curr_level = tree[row]
        for col in range(len(curr_level)):
            if prev_level[col] == "S" or prev_level[col] == "|":
                if curr_level[col] == "^":
                    if col - 1 >= 0:
                        curr_level[col - 1] = "|"
                    if col + 1 < len(curr_level):
                        curr_level[col + 1] = "|"
                    count += 1
                else:
                    curr_level[col] = "|"
        prev_level = curr_level
    return count


def count_timelines(tree):
    dp = [[0 for _ in range(len(tree[0]))] for _ in range(len(tree))]
    for i in range(len(tree[0])):
        if tree[0][i] == "S":
            dp[0][i] = 1

    prev_level = tree[0]
    for row in range(1, len(tree)):
        curr_level = tree[row]
        for col in range(len(curr_level)):
            if prev_level[col] == "S" or prev_level[col] == "|":
                if curr_level[col] == "^":
                    if col - 1 >= 0:
                        curr_level[col - 1] = "|"
                        if row < len(tree):
                            dp[row][col - 1] += dp[row - 1][col]
                    if col + 1 < len(curr_level):
                        curr_level[col + 1] = "|"
                        if row < len(tree):
                            dp[row][col + 1] += dp[row - 1][col]
                else:
                    curr_level[col] = "|"
                    if row < len(tree):
                        dp[row][col] += dp[row - 1][col]
        prev_level = curr_level
    for line in dp:
        print(line)
    for line in tree:
        print(line)
    return sum(dp[-1])


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.readlines()
    tree = [list(line.rstrip('\n')) for line in content]
    print(count_timelines(tree))
