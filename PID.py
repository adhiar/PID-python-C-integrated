import serial
import time
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import filedialog, ttk
import threading

# Serial Port configuration
serial_port = 'COM12'  # Adjust this for your device
baud_rate = 9600

# Global variables to store data
data = {"suhu": [], "setpoint": [], "KP": [], "KD": [], "KI": []}

def read_serial():
    """Reads data from serial port."""
    try:
        ser = serial.Serial(serial_port, baud_rate, timeout=1)
        while True:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if line:
                suhu, setpoint, KP, KD, KI = map(float, line.split('|'))
                data['suhu'].append(suhu)
                data['setpoint'].append(setpoint)
                data['KP'].append(KP)
                data['KD'].append(KD)
                data['KI'].append(KI)
                update_table()
            time.sleep(0.1)
    except serial.SerialException as e:
        print(f"Error reading serial port: {e}")

def update_table():
    """Updates the table in the GUI."""
    if len(data['suhu']) > 0:
        for i in range(len(data['suhu'])):
            table.insert('', 'end', values=(
                round(data['suhu'][i], 2),
                round(data['setpoint'][i], 2),
                round(data['KP'][i], 2),
                round(data['KD'][i], 2),
                round(data['KI'][i], 2),
            ))

def save_data():
    """Save data to a CSV file."""
    df = pd.DataFrame(data)
    file_path = filedialog.asksaveasfilename(defaultextension=".csv", 
                                             filetypes=[("CSV files", "*.csv")])
    if file_path:
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")

def update_plot(frame):
    """Update the plot."""
    if len(data['suhu']) > 0:
        ax.clear()
        ax.plot(data['suhu'], label='Suhu (Temperature)')
        ax.plot(data['setpoint'], label='Setpoint')
        ax.legend(loc='upper left')
        ax.set_title("Real-time Suhu vs Setpoint")
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Values")

def run_gui():
    """Run the GUI with a table and plot."""
    global root, table
    root = tk.Tk()
    root.title("Serial Data Plot and Table")

    # Create a table for data display
    columns = ('Suhu', 'Setpoint', 'KP', 'KD', 'KI')
    table = ttk.Treeview(root, columns=columns, show='headings')
    
    for col in columns:
        table.heading(col, text=col)
        table.column(col, minwidth=0, width=80, stretch=tk.NO)

    table.pack(padx=10, pady=10)

    # Create save button
    save_button = tk.Button(root, text="Save Data as CSV", command=save_data)
    save_button.pack(pady=10)

    root.protocol("WM_DELETE_WINDOW", lambda: [plt.close(), root.destroy()])
    root.mainloop()

# Start serial reading in a separate thread
serial_thread = threading.Thread(target=read_serial)
serial_thread.daemon = True
serial_thread.start()

# Create the plot
fig, ax = plt.subplots()
ani = FuncAnimation(fig, update_plot, interval=1000)

# Display the GUI in a separate thread to allow both plotting and GUI control
gui_thread = threading.Thread(target=run_gui)
gui_thread.daemon = True
gui_thread.start()

# Show plot
plt.show()
