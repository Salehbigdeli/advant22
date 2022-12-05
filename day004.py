def fully_contains():
    with open('inputs/day4.txt') as elfs:
        total_fully_contains = 0
        for line in elfs.readlines():
            alice_sections, bob_sections = line.strip().split(',')
            a_start, a_end = map(int, alice_sections.split('-'))
            b_start, b_end = map(int, bob_sections.split('-'))
            if a_end <= b_end and a_start >= b_start:
                total_fully_contains += 1
            elif b_end <= a_end and b_start >= a_start:
                total_fully_contains += 1

        return total_fully_contains


def any_overlap():
    with open('inputs/day4.txt') as elfs:
        total_overlaps_count = 0
        for line in elfs.readlines():
            alice_sections, bob_sections = line.strip().split(',')
            a_start, a_end = map(int, alice_sections.split('-'))
            b_start, b_end = map(int, bob_sections.split('-'))
            if b_start <= a_end <= b_end:
                total_overlaps_count += 1
            elif a_start <= b_end <= a_end:
                total_overlaps_count += 1

        return total_overlaps_count


print('part 1', fully_contains())
print('part 2', any_overlap())
