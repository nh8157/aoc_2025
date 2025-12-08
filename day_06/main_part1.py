def ops(matrix, col):
    def comp(acc, num, sign):
        match sign:
            case "*":
                return acc * num
            case "+":
                return acc + num
    sign = matrix[-1][col]
    acc = None
    for i in range(len(matrix)-1):
        num = int(matrix[i][col])
        if acc is None:
            acc = num
        else:
            acc = comp(acc, num, sign)
    return acc

def matrix_ops(matrix):
    matrix_sum = 0
    for i in range(len(matrix[0])):
        matrix_sum += ops(matrix, i)
    return matrix_sum

if __name__ == "__main__":
    with open("input.txt") as f:
        content = f.readlines()
    lines = [line.rstrip("\n").split() for line in content]
    # print(lines)
    print(matrix_ops(lines))
