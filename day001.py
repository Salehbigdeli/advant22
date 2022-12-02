import heapq


def elf_calories():
    with open('inputs/day1.txt') as elfs:
        elf_calorie = 0
        for line in elfs.readlines():
            if line == '\n':
                yield elf_calorie
                elf_calorie = 0
            else:
                elf_calorie += int(line.strip())


def get_top(k=3):
    q = []
    for ec in elf_calories():
        heapq.heappush(q, ec)
        if len(q) > k:
            heapq.heappop(q)
    return q


print('part 1', max(elf_calories()))

print('part 2', sum(get_top()))
