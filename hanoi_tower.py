def move_disk(disk, origin, to):
    print(f'Moving disk from {origin} to {to}')

def hanoi_tower(n, origin, to, aux):
    if n == 1:
        move_disk(1, origin, to)
        return

    hanoi_tower(n -1, origin, to, aux)
    move_disk(n, origin, to)
    hanoi_tower(n-1, aux, to, origin)

def hanoi_tower_of(n, origin, to):
    if n == 1:
        move_disk(1, origin, to)
    else:
        other = 6 - (origin + to)
        hanoi_tower_of(n-1, origin, other)
        move_disk(n, origin, to)
        hanoi_tower_of(n-1, other, to)


def hanoi_tower_dfs(n, origin, to, aux):
    stack = [(n, origin, to, aux, 0)]

    while stack:
        current = stack.pop()
        n, origin, to, aux, state = current

        if n == 1:
            move_disk(1, origin, to)
            continue

        if state == 0:
            stack.append((n, origin, to, aux, 1))
            stack.append((n -1 , origin, aux, to, 0))

        elif state == 1:
            move_disk(n, origin, to)
            stack.append((n -1 , aux, to, origin, 0))


# hanoi_tower(3, 'A', 'B', 'C')
# hanoi_tower_dfs(3, 'A', 'C', 'B')
hanoi_tower_of(3, 1, 3)