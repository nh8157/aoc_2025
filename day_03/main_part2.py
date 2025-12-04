def prefix_max(num):
    max_l = [0] * len(num)
    prev_max = num[0]
    for i in range(len(num)):
        prev_max = str(max(int(prev_max), int(num[i])))
        max_l[i] = prev_max
    return max_l


def postfix_max(num):
    max_l = [0] * len(num)
    post_max = num[-1]
    for i in range(len(num)-1, -1, -1):
        post_max = str(max(int(post_max), int(num[i])))
        max_l[i] = post_max
    return max_l


def line_joltage(num):
    pre = prefix_max(num)
    post = postfix_max(num)
    max_num = 0
    for i in range(len(pre)-1):
        curr_num = int(pre[i] + post[i+1])
        max_num = max(max_num, curr_num)
    return max_num


def joltage(nums):
    return sum([line_joltage(bat) for bat in nums])


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        print(joltage(lines))
