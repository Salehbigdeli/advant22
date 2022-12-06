import re
from collections import defaultdict


def parse_initial_stacks(lines):
    stacks = defaultdict(list)
    axis = lines[-1]
    stacks_data = lines[:-1]
    i = 1
    while True:
        if not str(i) in axis:
            break
        stack_idx = axis.find(str(i))
        for line in stacks_data[::-1]:
            elem = line[stack_idx]
            if elem == ' ':
                break
            stacks[i].append(elem)
        i += 1
    return dict(stacks)


def stack_command(command, stacks):
    pat = re.compile(r'move (\d*) from (\d*) to (\d*)')
    num, source, destination = map(int, re.match(pat, command).groups())
    for _ in range(num):
        item = stacks[source].pop()
        stacks[destination].append(item)


def bulk_command(command, stacks):
    pat = re.compile(r'move (\d*) from (\d*) to (\d*)')
    num, source, destination = map(int, re.match(pat, command).groups())
    items = stacks[source][-num:]
    stacks[source] = stacks[source][:-num]
    stacks[destination].extend(items)


def stack_tops(command_executor=stack_command):
    with open('inputs/day5.txt') as elfs:
        start_state_lines = []
        header_completed = False
        stacks = None
        for line in elfs.readlines():
            if line.startswith('move'):
                command_executor(line, stacks)
                continue
            if '\n' == line:
                header_completed = True
            if not header_completed:
                start_state_lines.append(line)
            if header_completed and stacks is None:
                stacks = parse_initial_stacks(start_state_lines)
    return ''.join(s.pop() for s in stacks.values())


print('part 1', stack_tops())
print('part 2', stack_tops(bulk_command))
