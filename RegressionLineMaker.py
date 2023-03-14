import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class RegressionLineGUI:
    def __init__(self, master):
        self.master = master
        master.title("Regression Line Maker")

        # Create GUI widgets
        self.x_label = tk.Label(master, text="Enter x values:")
        self.x_entry = tk.Entry(master)

        self.y_label = tk.Label(master, text="Enter y values:")
        self.y_entry = tk.Entry(master)

        self.plot_button = tk.Button(master, text="Plot Regression Line", command=self.plot_regression_line)

        # Layout GUI widgets using grid
        self.x_label.grid(row=0, column=0)
        self.x_entry.grid(row=0, column=1)

        self.y_label.grid(row=1, column=0)
        self.y_entry.grid(row=1, column=1)

        self.plot_button.grid(row=2, column=0, columnspan=2)

    def plot_regression_line(self):
        # Get x and y values from GUI entry widgets
        x_values = [float(x) for x in self.x_entry.get().split()]
        y_values = [float(y) for y in self.y_entry.get().split()]

        # Calculate regression line
        slope, intercept = np.polyfit(x_values, y_values, 1)
        regression_line = slope * np.array(x_values) + intercept

        # Plot data and regression line using matplotlib
        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.plot(x_values, y_values, 'o', label="Data")
        ax.plot(x_values, regression_line, label="Regression Line")
        ax.legend()

        # Create matplotlib canvas and add to GUI
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()
        canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)

# Create GUI window
root = tk.Tk()

# Create instance of RegressionLineGUI
app = RegressionLineGUI(root)

# Run GUI loop
root.mainloop()

