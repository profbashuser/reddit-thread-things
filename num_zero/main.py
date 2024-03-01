import tkinter as tk
import time

class ButtonTimerApp:
    def __init__(self, master):
        # Initialize the application
        self.master = master
        self.master.title("Button Timer")  # Set the title of the window
        
        # Create the button
        self.button = tk.Button(master, text="Start/End", command=self.button_pressed)
        self.button.pack(pady=20)  # Add the button to the window and add some padding
        
        # Initialize variables to track button presses and time
        self.last_press_time = None
        self.press_count = 0
        
        # Load the previous state (if any)
        self.load_state()
        
        # Create a label to display the time between button presses
        self.label = tk.Label(master, text="")
        self.label.pack(pady=10)  # Add the label to the window and add some padding
        
        # Start updating the label to show the time between button presses
        self.update_label()

    def button_pressed(self):
        # Handle button press event
        current_time = time.time()  # Get the current time
        
        # Calculate and display the time between button presses
        if self.press_count % 2 == 1:
            elapsed_time = current_time - self.last_press_time
            self.label.config(text=f"Time between presses: {elapsed_time:.2f} seconds")
        else:
            self.label.config(text="")
        
        # Update the last press time and press count
        self.last_press_time = current_time
        self.press_count += 1
        
        # Save the current state
        self.save_state()

    def load_state(self):
        # Load the previous state from a file
        try:
            with open("button_timer_state.txt", "r") as file:
                state = file.read().split(',')
                self.last_press_time = float(state[0])
                self.press_count = int(state[1])
        except FileNotFoundError:
            pass

    def save_state(self):
        # Save the current state to a file
        with open("button_timer_state.txt", "w") as file:
            file.write(f"{self.last_press_time},{self.press_count}")

    def update_label(self):
        # Update the label every second to show the time between button presses
        if self.last_press_time and self.press_count % 2 == 1:
            current_time = time.time()
            elapsed_time = current_time - self.last_press_time
            self.label.config(text=f"Time between presses: {elapsed_time:.2f} seconds")
        self.master.after(1000, self.update_label)

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    app = ButtonTimerApp(root)  # Create an instance of the ButtonTimerApp class
    root.mainloop()  # Start the main event loop to display the window and handle events
