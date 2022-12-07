class File:
    def __init__(self, size, name):
        self.name = name
        self.size = int(size)


class Dir:
    def __init__(self, name):
        self.name = name
        self.sub_dirs = set()
        self.files = set()
        self.parent = None

    @property
    def size(self):
        total_size = 0
        for f in self.files:
            total_size += f.size
        for d in self.sub_dirs:
            total_size += d.size
        return total_size

    def __repr__(self):
        return str((self.name, self.size))


def parse_command(cmd, cwd):
    cmd = cmd.strip()
    if cmd.startswith('$ ls'):
        return cwd
    if cmd.split()[2] == '..':
        return cwd.parent
    else:
        return [sd for sd in cwd.sub_dirs if sd.name == cmd.split()[2]][0]


def create_dir_tree():
    with open('inputs/day7.txt') as elfs:
        cwd = Dir(None)
        cwd.sub_dirs.add(Dir('/'))
        for line in elfs.readlines():
            if line.startswith('$'):
                cwd = parse_command(line, cwd)
            elif line.startswith('dir'):
                sub_dir = Dir(line.split()[1])
                sub_dir.parent = cwd
                cwd.sub_dirs.add(sub_dir)
            else:
                file = File(*line.strip().split())
                cwd.files.add(file)
        while cwd.name != '/':
            cwd = cwd.parent

        return cwd


def small_dirs_size(root=None):
    root = root or create_dir_tree()
    total_size = 0
    if root.size < 100000:
        total_size += root.size
    for d in root.sub_dirs:
        total_size += small_dirs_size(d)
    return total_size


def best_dir_size_to_delete():
    root = create_dir_tree()
    total_disk_size = 70000000
    desire_space = 30000000
    free_space = total_disk_size - root.size
    needed_space = desire_space - free_space
    return find_smallest_with_size(root, needed_space, min_found=root.size)


def find_smallest_with_size(root, needed_space, min_found):
    min_size = min_found
    if needed_space < root.size < min_size:
        min_size = root.size
    for d in root.sub_dirs:
        d_min = find_smallest_with_size(d, needed_space, min_size)
        if needed_space < d_min < min_size:
            min_size = d_min
    return min_size


print('part 1', small_dirs_size())
print('part 2', best_dir_size_to_delete())
