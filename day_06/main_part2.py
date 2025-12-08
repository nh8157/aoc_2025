def ops(nums, sign):
    print(nums)
    def comp(acc, num, sign):
        match sign:
            case "*":
                return acc * num
            case "+":
                return acc + num
    acc = None
    for i in range(len(nums)):
        num = int(nums[i])
        if acc is None:
            acc = num
        else:
            acc = comp(acc, num, sign)
    return acc

def matrix_ops(matrix):
    matrix_sum = 0
    sign = None
    nums = []
    for col in range(len(matrix[0])):
        if matrix[-1][col] == "*" or matrix[-1][col] == "+":
            matrix_sum += ops(nums, sign) if sign else 0
            nums = []
            sign = matrix[-1][col]
        s_sum = ""
        is_num = False
        for row in range(len(matrix)-2, -1, -1):
            d = matrix[row][col]
            if not is_num and d != " ":
                is_num = True
            if is_num:
                if d == " ":
                    d = "0"
                s_sum = d + s_sum
        if is_num and int(s_sum) != 0:
            nums.append(int(s_sum))
    return matrix_sum + ops(nums, sign)

if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.readlines()
    lines = [line.rstrip("\n") for line in content]
    # print(lines)
    print(matrix_ops(lines))
