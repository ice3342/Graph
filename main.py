from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import tkinter as tk

def main():
    app = Application()
    app.mainloop()

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Graphline")

#       Frames
        self.topbar = tk.Frame(self)
        self.topbar.grid(row=0, column=0, sticky="en")
        
        self.graph_frame = tk.Frame(self)
        self.graph_frame.grid(row=1, column=0)
#       -------------------------------
#       Graph
        self.fig, self.ax = plt.subplots()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas.get_tk_widget().grid(row=0, column=0)
#       -------------------------------
#       Toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.graph_frame, pack_toolbar = False)
        self.toolbar.grid(row=1, column=0, sticky="we")
#       -------------------------------
#       buttons, entrys and labels
        self.label = tk.Label(self,
                              text="separated numbers with commas",
                              font=("Times New Roman","15")) 
        self.label.grid(row=2, column=0)

        self.X_axis = Axis_entry(self.topbar, text="Enter X-axis")
        self.Y_axis = Axis_entry(self.topbar, text="Enter Y-axis")

        self.X_axis.grid(row=0, column=0)
        self.Y_axis.grid(row=1, column=0)

        self.add_line_btn = tk.Button(self.topbar,
                                      text="Add line",
                                      width=7, height=1,
                                      command=lambda:self.add_line(self.X_axis, self.Y_axis))
        self.add_line_btn.grid(row=0, column=1)
        self.bind("<Return>", lambda event: self.add_line(self.X_axis, self.Y_axis))

        self.clear_btn = tk.Button(self.topbar,
                             text="Clear", 
                             width=7, height=1,
                             command=self.clear,
                            #  background="#202020",
                            #  foreground="#EEEEEE"
                             )
        self.clear_btn.grid(row=1, column=1)

        self.dark_mode_btn = tk.Button(self.topbar,
                                  text="dark mode",
                                  command=self.dark_mode,
                                  width=7, height=1)
        self.dark_mode_btn.grid(row=0, column=3)
#       -------------------------------
# Functions
    def add_line(self, X_axis, Y_axis):
#       get and split the axis on commos
        X_axis = X_axis.get()
        Y_axis = Y_axis.get()

        X_axis = X_axis.split(",")
        Y_axis = Y_axis.split(",")
        print(X_axis, Y_axis)
#       -------------------------------

#       is the axis valid
        try:
            X_axis = [float(x) for x in X_axis]
            Y_axis = [float(y) for y in Y_axis]
        except ValueError:
            print("Invalid input")
            original_color = self.add_line_btn.cget("foreground")
            self.add_line_btn.config(foreground="red", text="Invalid input")
            self.after(1000, lambda: self.add_line_btn.config(foreground=original_color, text="Add line"))
            return
#       -------------------------------

#       try to plot the axis on self.ax if failed the change the label for a sec
        try:
            self.ax.plot(X_axis, Y_axis)
        except ValueError:
            print("axis do not match")
            original_label_color = self.label.cget("foreground")
            self.label.config(foreground="red")
            self.label.config(text="axis data amount do not match (exemple : x = 1, 2, 3 and y = 1, 2, 3, 4)")
            self.after(7000, lambda: self.label.config(foreground=original_label_color))
            self.after(7000, lambda: self.label.config(text="separated numbers with commas"))
            return
        self.canvas.draw()
#       --------------------------------------------------------------------------
#   clear the graphing board
    def clear(self):
        self.ax.clear()
        self.canvas.draw()
        print("clear")
#   ------------------------
# dark mode on-and-off
    def dark_mode(self):
        is_on = 0
        self.label.configure(fg="#ffffff", bg="#202020")
        self.add_line_btn.configure(fg="#ffffff",bg="#202020")
        self.clear_btn.configure(fg="#ffffff",bg="#202020")
        self.X_axis.configure(fg="#ffffff",bg="#202020")
        self.Y_axis.configure(fg="#ffffff",bg="#202020")
        self.dark_mode_btn.configure(fg="#ffffff",bg="#202020")
        self.configure(bg="#202020")
        self.ax.set_facecolor("#202020")
        self.ax.figure.set_facecolor("#303030")
        self.canvas.get_tk_widget().configure(bg="#202020")
        self.toolbar.configure(bg="#303030")
        for button in self.toolbar.winfo_children():
            button.configure(bg="#303030")
        self.canvas.draw()
        self.graph_frame.configure(bg="#202020")
        self.topbar.configure(bg="#202020")

# ----------

# the axis entrys for the functions of FucusIn-and-Out
class Axis_entry(tk.Entry):
#   on creation
    def __init__(self, parent, text=""):
        super().__init__(parent, width=69)

        self.text = text

        if self.get() == "":
            self.insert(0, text)
            self.config(foreground="grey")

        self.bind("<FocusIn>", self.In_n_Out)
        self.bind("<FocusOut>", self.In_n_Out)
#   -------------
#   the function for the text in the entry 
    def In_n_Out(self, event):
        if self.get() == self.text:
            self.delete(0, tk.END)
            self.config(foreground="black")
        elif self.get() == "":
            self.insert(0, self.text)
            self.config(foreground="grey")
#   ---------------------------------------
# ----------------------------------------------

if __name__ == "__main__":
    main()