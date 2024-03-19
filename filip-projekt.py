import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.display = tk.Entry(master, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        button_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
            ('+', 4, 0), ('-', 4, 2), ('*', 1, 3), ('/', 2, 3),
            ('=', 3, 3), ('Clear', 5, 0, 4)
        ]

        for text, row, col, *extra in button_texts:
            if text == 'Clear':
                btn = tk.Button(master, text=text, height=2, width=9 * 4, command=self.clear)
                btn.grid(row=row, column=col, columnspan=4)
            else:
                btn = tk.Button(master, text=text, height=2, width=9, command=lambda t=text: self.on_click(t))
                btn.grid(row=row, column=col)

    def on_click(self, text):
        if text == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            self.display.insert(tk.END, text)

    def clear(self):
        self.display.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()