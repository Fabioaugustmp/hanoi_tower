import matplotlib.pyplot as plt
import networkx as nx
import time

# Set interactive mode on for matplotlib (optional)
plt.ion()

def draw_pegs(pegs, step):
    G = nx.DiGraph()
    G.add_nodes_from(['A', 'B', 'C'])

    pos = {'A': (0, 0), 'B': (1, 0), 'C': (2, 0)}

    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=16)

    # Draw disks on each peg
    for peg, disks in pegs.items():
        for i, disk in enumerate(reversed(disks)):
            plt.text(
                pos[peg][0], -0.3 - 0.3*i,
                f'■' * disk,
                fontsize=12 + disk * 2,
                ha='center',
                color='black'
            )

    plt.title(f'Step {step}')
    plt.axis('off')
    plt.pause(0.8)
    plt.clf()

def hanoi_dfs_with_visual(n, origin, to, aux):
    stack = []
    stack.append((n, origin, to, aux, 0))

    # Pegs state (each is a list acting as a stack)
    pegs = { 'A': list(reversed(range(1, n+1))), 'B': [], 'C': [] }

    step = 0
    draw_pegs(pegs, step)

    while stack:
        current = stack.pop()
        n, origin, to, aux, state = current

        if n == 1:
            disk = pegs[origin].pop()
            pegs[to].append(disk)
            step += 1
            draw_pegs(pegs, step)
            continue

        if state == 0:
            stack.append((n, origin, to, aux, 1))          # Resume later
            stack.append((n - 1, origin, aux, to, 0))       # First recursive
        elif state == 1:
            disk = pegs[origin].pop()
            pegs[to].append(disk)
            step += 1
            draw_pegs(pegs, step)
            stack.append((n - 1, aux, to, origin, 0))       # Second recursive

    plt.ioff()
    plt.show()

# Run visualization
hanoi_dfs_with_visual(3, 'A', 'B', 'C')
