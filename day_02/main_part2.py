def find_min_repeated_num(num, step):
    l_num = len(num)
    if l_num % step == 0:
        front = int(num[:step])
        if str(front) * (l_num // step) >= num:
            return str(front) * (l_num // step)
        return str(front + 1) * (l_num // step)
    else:
        return str(10 ** (step - 1)) * (l_num // step + 1)

def find_max_repeated_num(num, step):
    l_num = len(num)
    if l_num % step == 0:
        front = int(num[:step])
        if str(front) * (l_num // step) <= num:
            return str(front) * (l_num // step)
        else:
            if front - 1 == 0:
                return ("9" * step) * (l_num // step - 1)
            return str(front - 1) * (l_num // step)
    else:
        return ("9" * step) * (l_num // step)

def sum_invalid_ids(rs):
    invalid_sum = 0

    for [left, right] in rs:
        invalid_set = set()
        for step in range(1, len(right) // 2 + 1):
            min_repeat = find_min_repeated_num(left, step)
            max_repeat = find_max_repeated_num(right, step)
            print(f"min: {min_repeat}, max: {max_repeat}, step: {step}")
            step_max = int("9" * step)
            while int(min_repeat) <= int(max_repeat):
                invalid_set.add(int(min_repeat))
                unit = str(min_repeat[:step])
                step_num = len(min_repeat) // step
                if int(unit) == step_max:
                    unit = str(10 ** (step - 1))
                    step_num += 1
                else:
                    unit = str(int(unit) + 1)
                min_repeat = unit * step_num
        invalid_sum += sum(invalid_set)
        print(invalid_set)

    return invalid_sum

if __name__ == "__main__":
    # sum_invalid_ids([["998", "1012"]])
    with open("input.txt", "r") as f:
        line = f.readline().strip('\n')
        ranges = [r.split('-') for r in line.split(',')]
        print(sum_invalid_ids(ranges))
