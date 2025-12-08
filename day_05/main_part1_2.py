def sort_and_combine_ranges(ranges: list[list[int]]) -> list[list[int]]:
    ranges.sort(key=lambda x: x[0])
    left = 0
    for right in range(1, len(ranges)):
        if ranges[left][1] >= ranges[right][0]:
            ranges[left][1] = max(ranges[left][1], ranges[right][1])
        else:
            left += 1
            ranges[left][0] = ranges[right][0]
            ranges[left][1] = ranges[right][1]
    return ranges[:left+1]


def is_valid_id(ranges, id):
    for [left, right] in ranges:
        if id >= left and id <= right:
            return True
        elif id < left:
            return False


def has_invalid_id(ranges):
    diff_sum = [(right-left+1) for [left, right] in ranges]
    return sum(diff_sum)


if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.read().strip("\n")

    ranges_txt, nums_txt = content.split("\n\n")
    ranges = [[int(n) for n in r.strip("\n").split("-")] for r in ranges_txt.splitlines()]
    nums = [int(n) for n in nums_txt.splitlines()]
    sorted_ranges = sort_and_combine_ranges(ranges)
    # part 1
    ctr = 0
    for n in nums:
        if is_valid_id(ranges, n):
            print("Is valid ID", n)
            ctr += 1
    print("Total valid IDs:", ctr)
    # part 2
    print(has_invalid_id(sorted_ranges))
