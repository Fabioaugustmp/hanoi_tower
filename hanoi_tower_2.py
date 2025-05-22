def move_disk(disk, origin, to, pegs, step):
    # Actually move the disk in our pegs data
    pegs[origin].pop()
    pegs[to].append(disk)

    # Print the step and the move
    print(f"Step {step}: move disk {disk} from {origin} → {to}")
    # Visualize current state
    for peg in ('A','B','C'):
        # print peg name and disks bottom→top
        print(f"  {peg}: {pegs[peg]}")
    print()  # blank line

def hanoi_tower_dfs(n, origin, to, aux):
    # Initialize stack and pegs
    stack = [(n, origin, to, aux, 0)]
    # pegs[peg] is a list of disks, bottom of tower = index 0
    pegs = {
        'A': list(reversed(range(1, n+1))),  # [n, n-1, …, 1]
        'B': [],
        'C': []
    }
    step = 0

    # Print initial state
    print("Initial state:")
    for peg in ('A','B','C'):
        print(f"  {peg}: {pegs[peg]}")
    print()

    while stack:
        n_cur, origin, to, aux, state = stack.pop()

        if n_cur == 1:
            step += 1
            # move disk 1
            move_disk(1, origin, to, pegs, step)
            continue

        if state == 0:
            # 1) after finishing moving n-1 to aux, come back here
            stack.append((n_cur, origin, to, aux, 1))
            # 2) first recursive: move n-1 from origin to aux
            stack.append((n_cur - 1, origin, aux, to, 0))

        elif state == 1:
            # now move the largest (n_cur) disk
            step += 1
            move_disk(n_cur, origin, to, pegs, step)
            # then move the n-1 from aux to target
            stack.append((n_cur - 1, aux, to, origin, 0))

# Example run
hanoi_tower_dfs(12, 'A', 'B', 'C')
