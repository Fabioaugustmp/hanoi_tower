import matplotlib.pyplot as plt
import time

def draw_pegs(pegs, n, step):
    plt.clf()
    peg_positions = {'A': 0, 'B': 1, 'C': 2}
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'cyan', 'magenta']

    for peg, disks in pegs.items():
        x = peg_positions[peg]
        for i, disk in enumerate(reversed(disks)):
            width = disk * 0.2
            height = 0.2
            y = i * height
            plt.barh(y=y, width=width, left=x - width / 2, height=height,
                     color=colors[disk % len(colors)], edgecolor='black')

    plt.title(f"Step {step}")
    plt.xticks([0, 1, 2], ['A', 'B', 'C'])
    plt.yticks([])
    plt.xlim(-0.5, 2.5)
    plt.ylim(0, n * 0.25)
    plt.pause(0.5)

def move_disk(disk, origin, to, pegs, step, n):
    pegs[origin].pop()
    pegs[to].append(disk)
    print(f"Step {step}: move disk {disk} from {origin} → {to}")
    draw_pegs(pegs, n, step)

def hanoi_tower_dfs(n, origin, to, aux):
    stack = [(n, origin, to, aux, 0)]
    pegs = {
        'A': list(reversed(range(1, n + 1))),  # bottom to top
        'B': [],
        'C': []
    }
    step = 0

    plt.ion()
    draw_pegs(pegs, n, step)

    while stack:
        n_cur, origin, to, aux, state = stack.pop()

        if n_cur == 1:
            step += 1
            move_disk(1, origin, to, pegs, step, n)
            continue

        if state == 0:
            stack.append((n_cur, origin, to, aux, 1))
            stack.append((n_cur - 1, origin, aux, to, 0))

        elif state == 1:
            step += 1
            move_disk(n_cur, origin, to, pegs, step, n)
            stack.append((n_cur - 1, aux, to, origin, 0))

    plt.ioff()
    plt.show()

# Run with n = 3
hanoi_tower_dfs(3, 'A', 'C', 'B')
