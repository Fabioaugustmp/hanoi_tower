import tkinter as tk
import time

# Constants
DELAY = 0.5  # seconds
DISK_HEIGHT = 20
PEG_WIDTH = 10
DISK_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class HanoiGUI:
    def __init__(self, root, num_disks):
        self.root = root
        self.num_disks = num_disks
        self.canvas_width = 600
        self.canvas_height = 300
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.pegs = {'A': [], 'B': [], 'C': []}
        self.peg_positions = {'A': 100, 'B': 300, 'C': 500}
        self.disk_ids = {}

        self.draw_pegs()
        self.init_disks()

    def draw_pegs(self):
        for x in self.peg_positions.values():
            self.canvas.create_rectangle(x - PEG_WIDTH//2, 100, x + PEG_WIDTH//2, 250, fill="black")

    def init_disks(self):
        for i in range(self.num_disks, 0, -1):
            width = i * 20
            x = self.peg_positions['A']
            y = 250 - len(self.pegs['A']) * DISK_HEIGHT
            disk = self.canvas.create_rectangle(x - width, y - DISK_HEIGHT, x + width, y,
                                                fill=DISK_COLORS[i % len(DISK_COLORS)])
            self.pegs['A'].append(i)
            self.disk_ids[i] = disk

    def move_disk(self, disk, origin, destination):
        print(f"Moving disk {disk} from {origin} to {destination}")
        self.pegs[origin].remove(disk)
        self.pegs[destination].append(disk)

        x_dest = self.peg_positions[destination]
        y_dest = 250 - (len(self.pegs[destination]) - 1) * DISK_HEIGHT
        width = disk * 20
        self.canvas.coords(self.disk_ids[disk],
                           x_dest - width, y_dest - DISK_HEIGHT,
                           x_dest + width, y_dest)
        self.root.update()
        time.sleep(DELAY)

    def hanoi(self, n, origin, destination, auxiliary):
        if n == 1:
            self.move_disk(1, origin, destination)
        else:
            self.hanoi(n - 1, origin, auxiliary, destination)
            self.move_disk(n, origin, destination)
            self.hanoi(n - 1, auxiliary, destination, origin)

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tower of Hanoi")

    num_disks = 3  # You can change this number
    gui = HanoiGUI(root, num_disks)
    root.after(1000, lambda: gui.hanoi(num_disks, 'A', 'B', 'C'))

    root.mainloop()
