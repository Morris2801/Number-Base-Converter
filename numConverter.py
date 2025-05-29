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

def TenToOct(decimal):
    if decimal == 0:
        return '0'
    baseEight = ''
    while decimal > 0:
        baseEight = str(decimal % 8) + baseEight
        decimal //= 8
    return baseEight

def OctToTen(octal):
    return int(str(octal), 8)

def TenToHex(decimal):
    if decimal == 0:
        return '0'
    baseHex = ''
    hexDigits = '0123456789ABCDEF'
    while decimal > 0:
        baseHex = hexDigits[decimal % 16] + baseHex
        decimal //= 16
    return baseHex

def HexToTen(hexa):
    return int(str(hexa), 16)

def convert():
    mode = var.get()
    try:
        if mode == "b2d":
            binary = entry.get()
            result = TwoToTen(binary)
            result_label.config(text=f"Decimal: {result}", fg="#7CFC00")
        elif mode == "d2b":
            decimal = int(entry.get())
            result = TenToTwo(decimal)
            result_label.config(text=f"Binary: {result}", fg="#00BFFF")
        elif mode == "d2o":
            decimal = int(entry.get())
            result = TenToOct(decimal)
            result_label.config(text=f"Octal: {result}", fg="#FFA500")
        elif mode == "o2d":
            octal = entry.get()
            result = OctToTen(octal)
            result_label.config(text=f"Decimal: {result}", fg="#FFA500")
        elif mode == "d2h":
            decimal = int(entry.get())
            result = TenToHex(decimal)
            result_label.config(text=f"Hex: {result}", fg="#FF69B4")
        elif mode == "h2d":
            hexa = entry.get()
            result = HexToTen(hexa)
            result_label.config(text=f"Decimal: {result}", fg="#FF69B4")
    except Exception as e:
        result_label.config(text="Invalid input.", fg="#FF4444")

root = tk.Tk()
root.title("Base Converter")
root.configure(bg="#222")
root.geometry("320x440")
root.resizable(True, True)

var = tk.StringVar(value="b2d")

tk.Label(root, text="Enter number", font=("Arial", 14, "bold"), fg="#FFD700", bg="#222").pack(pady=(25, 5))
entry = tk.Entry(root, font=("Consolas", 16), fg="#222", bg="#F5F5F5", justify="center", width=18, bd=2, relief="groove")
entry.pack(pady=5)

tk.Radiobutton(root, text="Binary to Decimal", variable=var, value="b2d",
               font=("Arial", 12), bg="#222", fg="#7CFC00", selectcolor="#444", activebackground="#333").pack(pady=2)
tk.Radiobutton(root, text="Decimal to Binary", variable=var, value="d2b",
               font=("Arial", 12), bg="#222", fg="#00BFFF", selectcolor="#444", activebackground="#333").pack(pady=2)
tk.Radiobutton(root, text="Decimal to Octal", variable=var, value="d2o",
               font=("Arial", 12), bg="#222", fg="#FFA500", selectcolor="#444", activebackground="#333").pack(pady=2)
tk.Radiobutton(root, text="Octal to Decimal", variable=var, value="o2d",
               font=("Arial", 12), bg="#222", fg="#FFA500", selectcolor="#444", activebackground="#333").pack(pady=2)
tk.Radiobutton(root, text="Decimal to Hex", variable=var, value="d2h",
               font=("Arial", 12), bg="#222", fg="#FF69B4", selectcolor="#444", activebackground="#333").pack(pady=2)
tk.Radiobutton(root, text="Hex to Decimal", variable=var, value="h2d",
               font=("Arial", 12), bg="#222", fg="#FF69B4", selectcolor="#444", activebackground="#333").pack(pady=2)

tk.Button(root, text="Convert", command=convert, font=("Arial", 13, "bold"),
          bg="#4CAF50", fg="white", activebackground="#388E3C", padx=10, pady=5, bd=0).pack(pady=20)

result_label = tk.Label(root, text="", font=("Consolas", 16), bg="#222")
result_label.pack(pady=(5, 10))

entry.focus_set()

root.mainloop()