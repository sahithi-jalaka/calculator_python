
from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Display
        self.result = StringVar()

        self.entry = Entry(
            self,
            textvariable=self.result,
            font=("Arial", 18),
            width=20,
            justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

        # Calculator buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3)
        ]

        for (text, row, col) in buttons:
            Button(
                self,
                text=text,
                font=("Arial", 14),
                width=5,
                command=lambda t=text: self.click(t)
            ).grid(row=row, column=col, padx=3, pady=3)

    def click(self, value):
        if value == "C":
            self.result.set("")

        elif value == "=":
            try:
                expression = self.result.get()
                if not expression or any(
                    c not in "0123456789.+-*/() " for c in expression
                ):
                    raise ValueError

                answer = eval(expression, {"__builtins__": {}}, {})
                self.result.set(str(answer))

            except (ValueError, SyntaxError, ZeroDivisionError, TypeError):
                self.result.set("Error")

        else:
            if self.result.get() == "Error":
                self.result.set("")
            self.result.set(self.result.get() + value)


root = Tk()
root.title("Simple Calculator")
root.geometry("330x300")

app = Application(root)

root.mainloop()
