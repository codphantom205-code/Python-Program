import tkinter as tk
def press(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + key)
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def clear():
    entry.delete(0, tk.END)
root = tk.Tk()
root.title("Basic Calculator")
entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0) ]
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=5, height=2, command=calculate).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, width=23, height=2, command=clear).grid(row=row, column=col, columnspan=4)
    else:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press(t)).grid(row=row, column=col)
root.mainloop()
