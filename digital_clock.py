import tkinter as tk
from time import strftime

# Create main window
root = tk.Tk()
root.title("🕒 Digital Clock")
root.geometry("400x200")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

# Clock label style
label = tk.Label(
    root,
    font=("Poppins", 50, "bold"),
    background="#1e1e2f",
    foreground="#00FFAA"
)
label.pack(anchor="center", pady=40)

# Function to update time
def update_time():
    time_string = strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    label.config(text=time_string)
    label.after(1000, update_time)  # Update every 1 second

# Start the clock
update_time()

# Footer
footer = tk.Label(
    root,
    text="Made with ❤️ in Python",
    font=("Poppins", 10),
    bg="#1e1e2f",
    fg="#888"
)
footer.pack(side="bottom")

# Run the app
root.mainloop()
