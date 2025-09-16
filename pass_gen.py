import tkinter as tk
from tkinter import ttk, messagebox
import secrets, string, math

def password_strength(password: str) -> str:
    char_space = 0
    if any(c.islower() for c in password): char_space += 26
    if any(c.isupper() for c in password): char_space += 26
    if any(c.isdigit() for c in password): char_space += 10
    if any(c in string.punctuation for c in password): char_space += len(string.punctuation)

    entropy = len(password) * math.log2(char_space) if char_space else 0

    if entropy < 40: return "Weak 🔴"
    elif 40 <= entropy < 60: return "Medium 🟡"
    elif 60 <= entropy < 80: return "Strong 🟢"
    else: return "Very Strong 🟣"

def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    chars = ""
    if use_lower: chars += string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation

    if not chars:
        raise ValueError("No character sets selected!")

    return ''.join(secrets.choice(chars) for _ in range(length))

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Advanced Password Generator")
        self.root.geometry("600x500")
        self.root.configure(bg="#1a1a2e")

        # Title
        title = tk.Label(root, text="Password Generator", font=("Segoe UI", 20, "bold"), bg="#1a1a2e", fg="white")
        title.pack(pady=10)

        # Options frame
        options_frame = tk.LabelFrame(root, text="Options", font=("Segoe UI", 12, "bold"), bg="#0f3460", fg="white", bd=2)
        options_frame.pack(pady=10, fill="x", padx=20)

        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digit_var = tk.BooleanVar(value=True)
        self.symbol_var = tk.BooleanVar(value=True)

        tk.Checkbutton(options_frame, text="Lowercase", variable=self.lower_var, bg="#0f3460", fg="white", selectcolor="#16213e").pack(side="left", padx=10, pady=5)
        tk.Checkbutton(options_frame, text="Uppercase", variable=self.upper_var, bg="#0f3460", fg="white", selectcolor="#16213e").pack(side="left", padx=10, pady=5)
        tk.Checkbutton(options_frame, text="Digits", variable=self.digit_var, bg="#0f3460", fg="white", selectcolor="#16213e").pack(side="left", padx=10, pady=5)
        tk.Checkbutton(options_frame, text="Symbols", variable=self.symbol_var, bg="#0f3460", fg="white", selectcolor="#16213e").pack(side="left", padx=10, pady=5)

        # Length selector
        length_frame = tk.Frame(root, bg="#1a1a2e")
        length_frame.pack(pady=10)
        tk.Label(length_frame, text="Password Length:", font=("Segoe UI", 12), bg="#1a1a2e", fg="white").pack(side="left")
        self.length_spin = tk.Spinbox(length_frame, from_=4, to=64, width=5, font=("Segoe UI", 12))
        self.length_spin.pack(side="left", padx=10)

        # Generate button
        self.generate_btn = tk.Button(root, text="Generate", font=("Segoe UI", 14, "bold"), bg="#e94560", fg="white", command=self.generate_passwords)
        self.generate_btn.pack(pady=10)

        # Output area
        self.output_box = tk.Text(root, height=10, width=50, font=("Consolas", 12), bg="#0d0d1e", fg="white")
        self.output_box.pack(pady=10)

        # Copy button
        self.copy_btn = tk.Button(root, text="Copy Selected", font=("Segoe UI", 12), bg="#16213e", fg="white", command=self.copy_password)
        self.copy_btn.pack(pady=5)

    def generate_passwords(self):
        self.output_box.delete("1.0", tk.END)
        length = int(self.length_spin.get())
        try:
            for i in range(5):  # Generate 5 passwords
                pwd = generate_password(
                    length,
                    self.lower_var.get(),
                    self.upper_var.get(),
                    self.digit_var.get(),
                    self.symbol_var.get()
                )
                strength = password_strength(pwd)
                self.output_box.insert(tk.END, f"{i+1}. {pwd}   ({strength})\n\n")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def copy_password(self):
        try:
            selected = self.output_box.get("sel.first", "sel.last").strip()
            if selected:
                self.root.clipboard_clear()
                self.root.clipboard_append(selected)
                messagebox.showinfo("Copied", "Password copied to clipboard!")
        except tk.TclError:
            messagebox.showwarning("Warning", "Please select a password to copy.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
