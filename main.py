import matplotlib.pyplot as plt
import tkinter as tk
import time as tm

def main():
    app = Application()
    app.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Graphline")
        self.config(background="#222222")

        self.label = tk.Label(self,
                              text="separated numbers by comma",
                              width=25,
                              background="#222222",
                              foreground="#EEEEEE")
        self.label.grid(row=2, column=0)

        X_axis = Axis_entry(self, text="Enter X-axis")
        Y_axis = Axis_entry(self, text="Enter Y-axis")

        X_axis.grid(row=0, column=0)
        Y_axis.grid(row=1, column=0)

        self.add_line_btn = tk.Button(self,
                                      text="Add line",
                                      width=7, height=1,
                                      background="#222222",
                                      foreground="#EEEEEE",
                                      command=lambda: self.add_line(X_axis, Y_axis))
        self.add_line_btn.grid(row=0, column=1)
        self.bind("<Return>", lambda event: self.add_line(X_axis, Y_axis))

        plot_btn = tk.Button(self,
                             text="Show graph", 
                             width=7, height=1,
                             command=plt.show,
                             background="#202020",
                             foreground="#EEEEEE")
        plot_btn.grid(row=1, column=1)
    
    def add_line(self, X_axis, Y_axis):
        X_axis = X_axis.get()
        Y_axis = Y_axis.get()

        X_axis = X_axis.split(",")
        Y_axis = Y_axis.split(",")
        print(X_axis, Y_axis)

        try:
            X_axis = [float(x) for x in X_axis]
            Y_axis = [float(y) for y in Y_axis]
        except ValueError:
            print("Invalid input")
            self.add_line_btn.config(foreground="red")
            self.add_line_btn.config(text="Invalid input")
            self.after(1000, lambda: self.add_line_btn.config(foreground="black"))
            self.after(1000, lambda: self.add_line_btn.config(text="Plot"))
            return
            
        try:
            plt.plot(X_axis, Y_axis)
        except ValueError:
            print("axis do not match")
            self.label.config(foreground="red")
            self.label.config(text="axis data amount do not match (exemple : x = 1, 2, 3 and y = 1, 2, 3, 4)")
            self.after(10000, lambda: self.label.config(foreground="black"))
            self.after(10000, lambda: self.label.config(text="separated numbers by comma"))
            return

class Axis_entry(tk.Entry):
    def __init__(self, parent, text=""):
        super().__init__(parent)

        self.text = text

        if self.get() == "":
            self.insert(0, text)
            self.config(foreground="grey")

        self.bind("<FocusIn>", self.In_n_Out)
        self.bind("<FocusOut>", self.In_n_Out)

    def In_n_Out(self, event):
        if self.get() == self.text:
            self.delete(0, tk.END)
            self.config(foreground="black")
        elif self.get() == "":
            self.insert(0, self.text)
            self.config(foreground="grey")

if __name__ == "__main__":
    main()