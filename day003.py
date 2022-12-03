def sum_property_type():
    total_property = 0
    with open('inputs/day3.txt') as sf:
        for line in sf.readlines():
            mid = len(line) // 2
            typ = list(set(line[:mid]) & set(line[mid:]))[0]
            total_property += ord(typ.lower()) - ord('a') + 1
            if typ.isupper():
                total_property += 26
    return total_property


def three_elves_property_type():
    total_property = 0
    with open('inputs/day3.txt') as sf:
        lines = []
        for line in sf.readlines():
            lines.append(set(line.strip()))
            if len(lines) == 3:
                typ = list(set(lines[0]) & set(lines[1]) & set(lines[2]))[0]
                total_property += ord(typ.lower()) - ord('a') + 1
                if typ.isupper():
                    total_property += 26
                lines = []
    return total_property


print('part 1', sum_property_type())
print('part 2', three_elves_property_type())
