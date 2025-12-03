def find_min_repeated_num(num):
    s_num = str(num)
    l_num = len(s_num)
    if len(s_num) % 2 == 0:
        front = s_num[:l_num // 2]
        back = s_num[l_num // 2:]
        if front >= back:
            return front * 2
        else:
            return str(int(front) + 1) * 2
    else:
        max_half = str(10 ** ((len(s_num)+1) // 2 - 1))
        return max_half + max_half

def find_max_repeated_num(num):
    s_num = str(num)
    l_num = len(s_num)
    if len(s_num) % 2 == 0:
        front = s_num[:l_num // 2]
        back = s_num[l_num // 2:]
        if front > back:
            return str(int(front) - 1) * 2
        else:
            return str(front * 2)
    else:
        return "9" * (len(s_num) - 1)

def sum_invalid_ids(ranges):
    invalid_sum = 0
    for [left, right] in ranges:
        min_repeated = find_min_repeated_num(left)
        max_repeated = find_max_repeated_num(right)
        print(f"Left: {left}, Right: {right}")
        print(f"Found min: {min_repeated}, max: {max_repeated}")
        if int(min_repeated) <= int(max_repeated):
            half_start = min_repeated[:len(min_repeated)//2]
            half_end = max_repeated[:len(max_repeated)//2]
            for i in range(int(half_start), int(half_end)+1):
                invalid_sum += int(str(i) + str(i))
    return invalid_sum

if __name__ == "__main__":
    with open("input.txt", "r") as f:
        line = f.readline().strip('\n')
        ranges = [r.split('-') for r in line.split(',')]
        print(sum_invalid_ids(ranges))
