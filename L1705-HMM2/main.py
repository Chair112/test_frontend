import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox
import math


class KerVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Хромоматематика: Ker(n)")
        self.root.resizable(width=False, height=False)
        self.root.bind("<F1>", self.show_thankfullness)
        self.root.bind("<F2>", self.show_help)

        # Метод переименован, чтобы не конфликтовать с атрибутом
        self.build_main_menu()

    def build_main_menu(self):
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Справка", menu=help_menu)
        help_menu.add_command(label="Текст с благодарностью", command=self.show_thankfullness)
        help_menu.add_command(label="Помощь", command=self.show_help)

        control_frame = ttk.Frame(self.root, width=200)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
        control_frame.pack_propagate(False)

        CHROMO_MODELS = ["HMM_N", "HMM_N2", "HMM_B", "HMM_R", "HMM_DN"]
        ttk.Label(control_frame, text="Модель:").pack(anchor="w")
        combobox = ttk.Combobox(control_frame, values=CHROMO_MODELS, width=15)
        combobox.pack(pady=5)
        combobox.current(0)

        ttk.Label(control_frame, text="Начало X:").pack(anchor="w")
        x_start = ttk.Entry(control_frame, width=6)
        x_start.insert(0, "1")
        x_start.pack(anchor="w", pady=5)

        ttk.Label(control_frame, text="Конец X:").pack(anchor="w")
        x_end = ttk.Entry(control_frame, width=6)
        x_end.insert(0, "50")
        x_end.pack(anchor="w", pady=5)

        ttk.Label(control_frame, text="Начало Y:").pack(anchor="w")
        y_start = ttk.Entry(control_frame, width=6)
        y_start.insert(0, "1")
        y_start.pack(anchor="w", pady=5)

        ttk.Label(control_frame, text="Конец Y:").pack(anchor="w")
        y_end = ttk.Entry(control_frame, width=6)
        y_end.insert(0, "50")
        y_end.pack(anchor="w", pady=5)

        ttk.Label(control_frame, text="N=").pack(anchor="w")
        modul_n = ttk.Entry(control_frame, width=6)
        modul_n.insert(0, "10")
        modul_n.pack(anchor="w", pady=5)
        
        ttk.Label(control_frame, text="A=").pack(anchor="w")
        arg_A = ttk.Entry(control_frame, width=6)
        arg_A.insert(0, "1")
        arg_A.pack(anchor="w", pady=5)

        fig = plt.Figure(figsize=(6, 4), dpi=100)
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        def draw():
            try:
                x1 = int(x_start.get())
                x2 = int(x_end.get())
                y1 = int(y_start.get())
                y2 = int(y_end.get())
                N = int(modul_n.get())
                A = int(arg_A.get())
            except ValueError:
                messagebox.showerror("Ошибка", "Введите корректные целые числа !")
                return

            if N <= 0:
                messagebox.showerror("Ошибка", "N должно быть больше 0 !")
                return
            if x1 >= x2 or y1 >= y2:
                messagebox.showerror("Ошибка", "Начальное значение больше конечного !")
                return
            if A < 1:
                messagebox.showerror("Ошибка", "Параметр A не может быть меньше 1 !")
                return
            
            x_values = list(range(x1, x2 + 1))
            y_values = list(range(y1, y2 + 1))

            cmap_name = 'viridis'
            colors = self.generate_colors(combobox.get(), x_values, y_values, N, A, cmap_name)

            self._draw_main_graph(fig, x_values, y_values, colors)
            canvas.draw()

        plot_button = ttk.Button(control_frame, text="Построить", command=draw)
        plot_button.pack(side=tk.BOTTOM, anchor='e', pady=10)

        # Автоматически рисуем карту при старте
        draw()

    def _draw_main_graph(self, fig, x_values, y_values, colors):
        fig.clear()
        ax = fig.add_subplot(111)
        ax.imshow(
            colors,
            aspect='auto',
            origin='lower',
            extent=[x_values[0], x_values[-1], y_values[0], y_values[-1]],
            interpolation='nearest'
        )
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('Функциональная зависимость: A*sin(X+Y)')
        fig.tight_layout()
    
    def calc_func_dep(self,X,Y,A):
        return A*math.sin(X+Y)

    def show_thankfullness(self, event=None):
        thankfullness_text = (
            "Выражаю свою огромную благодарность родителям -\n"
            "Прокофьеву Константину и Прокофьевой Ларисе за любовь,\n"
            "поддержку и хорошее воспитание. Ещё раз благодарю вас от\n"
            "всего сердца за веру в меня и огромную помощь на моём пути.\n"
            "© Максим Прокофьев"
        )
        thankfullness_window = tk.Toplevel(self.root)
        thankfullness_window.title("Благодарность родителям")
        label = tk.Label(thankfullness_window, text=thankfullness_text,
                         justify=tk.LEFT, padx=10, pady=10)
        label.pack()

    def show_help(self, event=None):
        help_text = (
            "Хромоматематическое моделирование"
            "Для использования программы:\n"
            "1.впишите диапазоныв поля для начал и концов диапазонов x и y\n"
            "2.укажите в нужное поле N - унификационный нормирующиймножитель для дискретного сведения результата\n"
            "3.Впишите в соответствующие поле параметр A, который нужен для расчёта функциональной зависимости \n"
            "4.Нажмите кнопку с надписью 'Построить'\n"
            "Прокофьев Максим"
        )
        help_window = tk.Toplevel(self.root)
        help_window.title("Помощь")
        label = tk.Label(help_window, text=help_text,
                         justify=tk.LEFT, padx=10, pady=10)
        label.pack()

    def ker(self, a):
        a = abs(a)
        while a >= 10:
            a = sum(int(digit) for digit in str(a))
        return a

    def generate_colors(self, model, x_values, y_values, N=10, A=1, cmap_name='viridis'):
        """
        Генерация цветов для тепловой карты.
        
        Параметры:
            model      - название модели ('HMM_N', 'HMM_N2', 'HMM_B', 'HMM_R', 'HMM_DN')
            x_values   - список значений по оси X
            y_values   - список значений по оси Y
            N          - модуль
            cmap_name  - имя colormap из matplotlib (используется только если модель его требует)
        
        Возвращает:
            numpy-массив формы (len(y_values), len(x_values), 4) с RGBA-цветами
        """
        height = len(y_values)
        width = len(x_values)
        colors = np.zeros((height, width, 4))

        for i, y in enumerate(y_values):
            for j, x in enumerate(x_values):
                colors[i, j] = self._compute_color(model, x, y, N, A, width, height)

        return colors


    def _compute_color(self, model, x, y, N, A , width, height):
        if model == "HMM_N":
            # Оттенки от чёрного до белого, количество оттенков = длине диапазона
            # Используем максимальную длину диапазона
            max_len = max(width, height)
            value = (self.calc_func_dep(x,y,A)) % max_len
            gray = value / (max_len - 1) if max_len > 1 else 0.5
            return (gray, gray, gray, 1.0)

        elif model == "HMM_N2":
            # Градиент от синего через белый к красному
            max_len = max(width, height)
            value = (self.calc_func_dep(x**2,y**2,A)) % max_len
            t = value / (max_len - 1) if max_len > 1 else 0.5
            
            # От 0.0 до 0.5: синий → белый
            # От 0.5 до 1.0: белый → красный
            if t <= 0.5:
                # Синий (0,0,1) → Белый (1,1,1)
                ratio = t / 0.5
                r = ratio
                g = ratio
                b = 1.0
            else:
                # Белый (1,1,1) → Красный (1,0,0)
                ratio = (t - 0.5) / 0.5
                r = 1.0
                g = 1.0 - ratio
                b = 1.0 - ratio
            return (r, g, b, 1.0)

        elif model == "HMM_B":
            # Градиент от фиолетового до красного
            value = (self.calc_func_dep(x,y,A)) % N
            t = value / N
            
            # Фиолетовый (1,0,1) → Красный (1,0,0)
            # Меняется только синий канал от 1 до 0
            r = 1.0
            g = 0.0
            b = 1.0 - t
            return (r, g, b, 1.0)

        elif model == "HMM_R":
            # Радужный градиент: красный → жёлтый → зелёный → голубой → синий → фиолетовый
            value = self.ker(self.calc_func_dep(x**2,y**2,A))
            t = value / 9  # ker даёт значения 1-9, нормализуем в [0, 1]
            
            # HSV-модель: Hue от 0 (красный) до 0.83 (фиолетовый)
            # Преобразуем HSV в RGB
            h = t * 0.83  # 0.83 соответствует фиолетовому
            s = 1.0
            v = 1.0
            
            # HSV to RGB conversion
            i = int(h * 6)
            f = (h * 6) - i
            p = v * (1 - s)
            q = v * (1 - f * s)
            t_val = v * (1 - (1 - f) * s)
            
            i = i % 6
            if i == 0:
                r, g, b = v, t_val, p
            elif i == 1:
                r, g, b = q, v, p
            elif i == 2:
                r, g, b = p, v, t_val
            elif i == 3:
                r, g, b = p, q, v
            elif i == 4:
                r, g, b = t_val, p, v
            else:  # i == 5
                r, g, b = v, p, q
            
            return (r, g, b, 1.0)

        elif model == "HMM_DN":
            # Дискретные цвета по модулю N
            value = (self.calc_func_dep(x,y,A)) % N  # целое число от 0 до N-1
            
            # Используем HSV для создания N различных цветов
            h = value / N
            s = 1.0
            v = 1.0
            
            # HSV to RGB conversion
            i = int(h * 6)
            f = (h * 6) - i
            p = v * (1 - s)
            q = v * (1 - f * s)
            t_val = v * (1 - (1 - f) * s)
            
            i = i % 6
            if i == 0:
                r, g, b = v, t_val, p
            elif i == 1:
                r, g, b = q, v, p
            elif i == 2:
                r, g, b = p, v, t_val
            elif i == 3:
                r, g, b = p, q, v
            elif i == 4:
                r, g, b = t_val, p, v
            else:  # i == 5
                r, g, b = v, p, q
            
            return (r, g, b, 1.0)

        else:
            return (0.5, 0.5, 0.5, 1.0)


if __name__ == "__main__":
    root = tk.Tk()
    app = KerVisualizerApp(root)
    root.mainloop()