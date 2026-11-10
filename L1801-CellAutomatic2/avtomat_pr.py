import tkinter as tk

# Правила: имя -> (рождение, выживание)
RULES = {
    "Conway": (set([3]), set([2, 3])),
    "HighLife": (set([3, 6]), set([2, 3])),
    "Seeds": (set([2]), set([])),
    "Day&Night": (set([3, 6, 7, 8]), set([3, 4, 6, 7, 8])),
}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AmCellAutomatic2")
        
        self.ROWS, self.COLS = 30, 30
        self.CELL_SIZE = 20
        self.running = False
        self.speed = 200
        
        # Сетка: True - живая, False - мёртвая
        self.grid = [[False] * self.COLS for _ in range(self.ROWS)]
        
        self._init_ui()
        self._set_rule("Conway")
        self._draw_glider()
        self._draw()
    
    def _init_ui(self):
        # Панель управления
        panel = tk.Frame(self)
        panel.pack(pady=5)
        
        tk.Label(panel, text="Правило:").pack(side=tk.LEFT, padx=5)
        self.rule_var = tk.StringVar()
        combo = tk.OptionMenu(panel, self.rule_var, *RULES.keys(), command=self._set_rule)
        combo.pack(side=tk.LEFT, padx=5)
        
        tk.Button(panel, text="Старт", command=self._start).pack(side=tk.LEFT, padx=2)
        tk.Button(panel, text="Стоп", command=self._stop).pack(side=tk.LEFT, padx=2)
        tk.Button(panel, text="Шаг", command=self._step).pack(side=tk.LEFT, padx=2)
        tk.Button(panel, text="Очистить", command=self._clear).pack(side=tk.LEFT, padx=2)
        
        # Холст
        self.canvas = tk.Canvas(self, 
            width=self.COLS * self.CELL_SIZE, 
            height=self.ROWS * self.CELL_SIZE)
        self.canvas.pack()
        
        # Привязка мыши
        self.canvas.bind("<B1-Motion>", self._draw_mouse)
        self.canvas.bind("<Button-1>", self._draw_mouse)
    
    def _set_rule(self, name):
        self.birth, self.survive = RULES[name]
        self.info = f"B:{sorted(self.birth)} S:{sorted(self.survive)}"
        self.title(f"AmCellAutomatic2 - {name} ({self.info})")
    
    def _count_neighbors(self, r, c):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.ROWS and 0 <= nc < self.COLS:
                    count += self.grid[nr][nc]
        return count
    
    def _step(self):
        new_grid = [[False] * self.COLS for _ in range(self.ROWS)]
        for r in range(self.ROWS):
            for c in range(self.COLS):
                n = self._count_neighbors(r, c)
                if self.grid[r][c]:
                    new_grid[r][c] = n in self.survive
                else:
                    new_grid[r][c] = n in self.birth
        self.grid = new_grid
        self._draw()
    
    def _tick(self):
        if self.running:
            self._step()
            self.after(self.speed, self._tick)
    
    def _start(self):
        if not self.running:
            self.running = True
            self._tick()
    
    def _stop(self):
        self.running = False
    
    def _clear(self):
        self._stop()
        self.grid = [[False] * self.COLS for _ in range(self.ROWS)]
        self._draw()
    
    def _draw(self):
        self.canvas.delete("all")
        for r in range(self.ROWS):
            for c in range(self.COLS):
                x0, y0 = c * self.CELL_SIZE, r * self.CELL_SIZE
                x1, y1 = x0 + self.CELL_SIZE, y0 + self.CELL_SIZE
                color = "green" if self.grid[r][c] else "yellow"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")
    
    def _draw_mouse(self, event):
        c = event.x // self.CELL_SIZE
        r = event.y // self.CELL_SIZE
        if 0 <= r < self.ROWS and 0 <= c < self.COLS:
            self.grid[r][c] = True
            self._draw()
    
    def _draw_glider(self):
        # Фигура с картинки
        pattern = [(0, 3), (1, 1), (1, 3), (2, 2), (2, 3)]
        for dr, dc in pattern:
            self.grid[dr][dc] = True

if __name__ == "__main__":
    App().mainloop()