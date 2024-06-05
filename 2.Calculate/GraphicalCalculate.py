import tkinter as tk

def button_click(symbol):
    current = result_text.get()
    result_text.delete(0, tk.END)
    result_text.insert(tk.END, current + symbol)

def clear():
    result_text.delete(0, tk.END)

def calculate():
    expression = result_text.get()
    try:
        result = eval(expression)
        result_text.delete(0, tk.END)
        result_text.insert(tk.END, str(result))
    except:
        result_text.delete(0, tk.END)
        result_text.insert(tk.END, "錯誤")

# 創建主視窗
root = tk.Tk()
root.title("簡單計算器")

# 輸出框
result_text = tk.Entry(root, width=30, borderwidth=5, bg="white", fg="black")
result_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# 按鈕
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=10, command=lambda symbol=text: button_click(symbol))
    button.grid(row=row, column=column)

# 清除按鈕
clear_button = tk.Button(root, text="清除", padx=60, pady=10, command=clear)
clear_button.grid(row=5, column=0, columnspan=2)

# 計算按鈕
equal_button = tk.Button(root, text="計算", padx=60, pady=10, command=calculate)
equal_button.grid(row=5, column=2, columnspan=2)

root.mainloop()
