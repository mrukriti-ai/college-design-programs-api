import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        
        # Calculator state
        self.current_number = ""
        self.previous_number = ""
        self.operation = ""
        self.should_reset = False
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
        
        # Configure grid weights
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def create_display(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="#2a2a2a", relief="raised", bd=2)
        display_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        # Previous calculation display
        self.previous_label = tk.Label(
            display_frame, 
            text="", 
            font=("Arial", 14), 
            bg="#2a2a2a", 
            fg="#888888",
            anchor="e",
            padx=10
        )
        self.previous_label.pack(fill="x", pady=(10, 5))
        
        # Current number display
        self.display_label = tk.Label(
            display_frame, 
            text="0", 
            font=("Arial", 32, "bold"), 
            bg="#2a2a2a", 
            fg="white",
            anchor="e",
            padx=10
        )
        self.display_label.pack(fill="x", pady=(0, 10))
        
    def create_buttons(self):
        # Button configurations
        button_configs = [
            ("C", 1, 0, "#ff3b30", "white"),
            ("⌫", 1, 1, "#ff9500", "white"),
            ("%", 1, 2, "#ff9500", "white"),
            ("÷", 1, 3, "#ff9500", "white"),
            
            ("7", 2, 0, "#333333", "white"),
            ("8", 2, 1, "#333333", "white"),
            ("9", 2, 2, "#333333", "white"),
            ("×", 2, 3, "#ff9500", "white"),
            
            ("4", 3, 0, "#333333", "white"),
            ("5", 3, 1, "#333333", "white"),
            ("6", 3, 2, "#333333", "white"),
            ("−", 3, 3, "#ff9500", "white"),
            
            ("1", 4, 0, "#333333", "white"),
            ("2", 4, 1, "#333333", "white"),
            ("3", 4, 2, "#333333", "white"),
            ("+", 4, 3, "#ff9500", "white"),
            
            ("±", 5, 0, "#333333", "white"),
            ("0", 5, 1, "#333333", "white"),
            (".", 5, 2, "#333333", "white"),
            ("=", 5, 3, "#34c759", "white")
        ]
        
        # Create buttons
        for (text, row, col, bg_color, fg_color) in button_configs:
            button = tk.Button(
                self.root,
                text=text,
                font=("Arial", 18, "bold"),
                bg=bg_color,
                fg=fg_color,
                relief="flat",
                bd=0,
                padx=20,
                pady=20,
                cursor="hand2"
            )
            button.grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            
            # Bind events
            if text in "0123456789.":
                button.config(command=lambda t=text: self.add_number(t))
            elif text in "+−×÷":
                button.config(command=lambda t=text: self.set_operation(t))
            elif text == "=":
                button.config(command=self.calculate)
            elif text == "C":
                button.config(command=self.clear)
            elif text == "⌫":
                button.config(command=self.backspace)
            elif text == "±":
                button.config(command=self.toggle_sign)
            elif text == "%":
                button.config(command=self.percentage)
            
            # Hover effects
            button.bind("<Enter>", lambda e, btn=button: self.on_hover_enter(btn))
            button.bind("<Leave>", lambda e, btn=button: self.on_hover_leave(btn))
        
        # Configure grid weights for buttons
        for i in range(1, 6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def on_hover_enter(self, button):
        """Add hover effect to button"""
        current_bg = button.cget("bg")
        if current_bg == "#333333":
            button.config(bg="#444444")
        elif current_bg == "#ff9500":
            button.config(bg="#ffaa33")
        elif current_bg == "#ff3b30":
            button.config(bg="#ff4d40")
        elif current_bg == "#34c759":
            button.config(bg="#40d465")
    
    def on_hover_leave(self, button):
        """Remove hover effect from button"""
        current_bg = button.cget("bg")
        if current_bg == "#444444":
            button.config(bg="#333333")
        elif current_bg == "#ffaa33":
            button.config(bg="#ff9500")
        elif current_bg == "#ff4d40":
            button.config(bg="#ff3b30")
        elif current_bg == "#40d465":
            button.config(bg="#34c759")
    
    def add_number(self, number):
        """Add a number to the current display"""
        if self.should_reset:
            self.current_number = ""
            self.should_reset = False
        
        if number == "." and "." in self.current_number:
            return
        
        if self.current_number == "0" and number != ".":
            self.current_number = number
        else:
            self.current_number += number
        
        self.update_display()
    
    def set_operation(self, op):
        """Set the operation to perform"""
        if self.current_number:
            if self.previous_number:
                self.calculate()
            
            self.previous_number = self.current_number
            self.operation = op
            self.should_reset = True
            
            # Update previous display
            operation_symbols = {"+": "+", "−": "-", "×": "×", "÷": "÷"}
            self.previous_label.config(text=f"{self.previous_number} {operation_symbols[op]}")
    
    def calculate(self):
        """Perform the calculation"""
        if not self.current_number or not self.previous_number or not self.operation:
            return
        
        try:
            prev = float(self.previous_number)
            current = float(self.current_number)
            
            if self.operation == "+":
                result = prev + current
            elif self.operation == "−":
                result = prev - current
            elif self.operation == "×":
                result = prev * current
            elif self.operation == "÷":
                if current == 0:
                    self.display_label.config(text="Error")
                    return
                result = prev / current
            
            # Format result
            if result.is_integer():
                result = int(result)
            else:
                result = round(result, 10)  # Remove trailing zeros
            
            self.current_number = str(result)
            self.previous_number = ""
            self.operation = ""
            self.should_reset = True
            
            # Clear previous display
            self.previous_label.config(text="")
            self.update_display()
            
        except ValueError:
            self.display_label.config(text="Error")
    
    def clear(self):
        """Clear all values"""
        self.current_number = ""
        self.previous_number = ""
        self.operation = ""
        self.should_reset = False
        self.display_label.config(text="0")
        self.previous_label.config(text="")
    
    def backspace(self):
        """Remove the last character"""
        if self.should_reset:
            return
        
        if len(self.current_number) > 1:
            self.current_number = self.current_number[:-1]
        else:
            self.current_number = ""
        
        self.update_display()
    
    def toggle_sign(self):
        """Toggle the sign of the current number"""
        if self.current_number and self.current_number != "0":
            if self.current_number.startswith("-"):
                self.current_number = self.current_number[1:]
            else:
                self.current_number = "-" + self.current_number
            self.update_display()
    
    def percentage(self):
        """Convert current number to percentage"""
        if self.current_number:
            try:
                value = float(self.current_number)
                result = value / 100
                if result.is_integer():
                    result = int(result)
                self.current_number = str(result)
                self.update_display()
            except ValueError:
                self.display_label.config(text="Error")
    
    def update_display(self):
        """Update the display with current number"""
        if self.current_number:
            self.display_label.config(text=self.current_number)
        else:
            self.display_label.config(text="0")

def main():
    root = tk.Tk()
    root.configure(bg="#1a1a1a")
    
    # Center the window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"{width}x{height}+{x}+{y}")
    
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main() 