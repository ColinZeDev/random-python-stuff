from tkinter import messagebox
import tkinter as tk
import platform

class App:
    def __init__(self, *, dev_mode: bool = False):
        self.devmode = dev_mode

        self.root = tk.Tk()
        self.root.title("Percent Change Calculator")
        self.root.geometry(f"{self.root.winfo_screenwidth()//4}x{self.root.winfo_screenheight()//2}")

        if self.devmode:
            print(f"Window init done. geometry: {self.root.winfo_screenwidth()//4}x{self.root.winfo_screenheight()//2}")

        self.titlelabel = tk.Label(self.root, text="Percent Change Calculator", font=("Arial", 24))
        self.titlelabel.pack(pady=10)

        self.oldvaltextbox = tk.Entry(self.root, font=("Arial", 14), fg="gray")
        self.oldvaltextbox.insert(0, "enter old value...")
        self.oldvaltextbox.bind("<FocusIn>", lambda e: self._clear_placeholder(e, self.oldvaltextbox, "enter old value..."))
        self.oldvaltextbox.bind("<FocusOut>", lambda e: self._restore_placeholder(e, self.oldvaltextbox, "enter old value..."))
        self.oldvaltextbox.pack(pady=10, ipadx=5, ipady=5)

        self.newvaltextbox = tk.Entry(self.root, font=("Arial", 14), fg="gray")
        self.newvaltextbox.insert(0, "enter new value...")
        self.newvaltextbox.bind("<FocusIn>", lambda e: self._clear_placeholder(e, self.newvaltextbox, "enter new value..."))
        self.newvaltextbox.bind("<FocusOut>", lambda e: self._restore_placeholder(e, self.newvaltextbox, "enter new value..."))
        self.newvaltextbox.pack(pady=10, ipadx=5, ipady=5)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 18))
        self.result_label.pack(pady=20)

        self.calc_button = tk.Button(self.root, text="Calculate", font=("Arial", 16), command=self._calculate)
        self.calc_button.pack(pady=10)

    def _clear_placeholder(self, event, widget, text):
        if widget.get() == text:
            widget.delete(0, tk.END)
            widget.config(fg="black")

    def _restore_placeholder(self, event, widget, text):
        if not widget.get():
            widget.insert(0, text)
            widget.config(fg="gray")

    @staticmethod
    def __do_math(old_val: int | float, new_val: int | float):
        pc = (new_val - old_val) / old_val * 100
        pc_str = f"{abs(pc):.2f}%"

        if pc > 0:
            return f"Up {pc_str}"
        elif pc < 0:
            return f"Down {pc_str}"
        else:
            return "No change"

    def _calculate(self):
        try:
            old_text = self.oldvaltextbox.get()
            new_text = self.newvaltextbox.get()

            if old_text.startswith("enter") or new_text.startswith("enter"):
                self.result_label.config(text="Enter both numbers!")
                return

            old_val = float(old_text)
            new_val = float(new_text)

            result = self.__do_math(old_val, new_val)
            self.result_label.config(text=result)

        except ValueError:
            self.result_label.config(text="Invalid input")

    def run(self, n: int = 0):
        self.root.mainloop(n)


if __name__ == "__main__":
    app = App(dev_mode=True)
    if platform.platform().lower() == 'linux':
        c = messagebox.askyesno('Confirm', 'This app may be unstable on linux, Run?')
        if c:
            app.run()
    else:
        app.run()
