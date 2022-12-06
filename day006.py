def encoding_begins_at(distinct=4):
    with open('inputs/day6.txt') as elfs:
        for line in elfs.readlines():
            for i in range(len(line)):
                if len(set(line[i:i + distinct])) == distinct:
                    return i + distinct


print('part 1', encoding_begins_at())
print('part 2', encoding_begins_at(14))
