import tkinter as tk

def TenToTwo(decimal):
    baseTwo = ''
    if decimal == 0: 
        return '0'
    while decimal > 0: 
        baseTwo = str(decimal % 2) + baseTwo
        decimal //= 2
    return baseTwo

def TwoToTen(binary):
    sum = 0
    binaryStr = str(binary)
    wholeStr, period, decimalStr = binaryStr.partition('.')
    lstWhole = []
    for i in range(0,len(wholeStr)): 
        lstWhole.append(int(wholeStr[i]))
    maxIndex = len(lstWhole) - 1
    for value in lstWhole: 
        sum += value * (2 ** maxIndex)
        maxIndex -= 1
    whole = sum
    sum = 0
    lstDec = []
    for i in range(0,len(decimalStr)): 
        lstDec.append(int(decimalStr[i]))
    maxIndex = -1
    for value in lstDec: 
        sum += value * (2 ** maxIndex)
        maxIndex -= 1
    dec = sum % 1
    return whole + dec

def convert():
    if var.get() == "b2d":
        try:
            binary = entry.get()
            result = TwoToTen(binary)
            result_label.config(text=f"Decimal: {result}", fg="#7CFC00")
        except Exception as e:
            result_label.config(text="Invalid binary number.", fg="#FF4444")
    else:
        try:
            decimal = int(entry.get())
            result = TenToTwo(decimal)
            result_label.config(text=f"Binary: {result}", fg="#00BFFF")
        except Exception as e:
            result_label.config(text="Invalid decimal number.", fg="#FF4444")

root = tk.Tk()
root.title("Base Converter")
root.configure(bg="#222")
root.geometry("350x320")
root.resizable(False, False)

var = tk.StringVar(value="b2d")

tk.Label(root, text="Enter number:", font=("Arial", 14, "bold"), fg="#FFD700", bg="#222").pack(pady=(25, 5))
entry = tk.Entry(root, font=("Consolas", 16), fg="#222", bg="#F5F5F5", justify="center", width=18, bd=2, relief="groove")
entry.pack(pady=5)

tk.Radiobutton(root, text="Binary to Decimal", variable=var, value="b2d",
               font=("Arial", 12), bg="#222", fg="#7CFC00", selectcolor="#444", activebackground="#333").pack(pady=2)
tk.Radiobutton(root, text="Decimal to Binary", variable=var, value="d2b",
               font=("Arial", 12), bg="#222", fg="#00BFFF", selectcolor="#444", activebackground="#333").pack(pady=2)

tk.Button(root, text="Convert", command=convert, font=("Arial", 13, "bold"),
          bg="#4CAF50", fg="white", activebackground="#388E3C", padx=10, pady=5, bd=0).pack(pady=20)

# Result label (initially empty)
result_label = tk.Label(root, text="", font=("Consolas", 16), bg="#222")
result_label.pack(pady=(5, 10))

entry.focus_set()

root.mainloop()