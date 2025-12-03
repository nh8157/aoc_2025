def password(rotations: list[str]) -> int:
    pos = 50
    pas = 0

    for rot in rotations:
        d = rot[0]
        steps = int(rot[1:])
        steps = steps if d == "R" else 100 - steps
        pos = (pos + steps) % 100
        if pos == 0:
            pas += 1

    return pas


def password_p2(rotations: list[str]) -> int:
    pos = 50
    pas = 0

    for rot in rotations:
        d = -1 if rot[0] == 'L' else 1
        steps = int(rot[1:])
        next_pos = pos + d * steps
        if next_pos >= 100:
            pas += next_pos // 100
            print("pos", pas, "old", pos, "new", next_pos)
        elif next_pos <= 0:
            pas += abs(next_pos) // 100
            if pos > 0:
                pas += 1
            print("neg", pas, "old", pos, "new", next_pos)
        pos = next_pos % 100
    return pas


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        rotations = [l.strip('\n') for l in lines]
        print(password_p2(rotations))
