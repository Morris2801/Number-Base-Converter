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
            result_label.config(text=f"Decimal: {result}", fg="#00B8D9")
        elif mode == "d2b":
            decimal = int(entry.get())
            result = TenToTwo(decimal)
            result_label.config(text=f"Binary: {result}", fg="#00B8D9")
        elif mode == "d2o":
            decimal = int(entry.get())
            result = TenToOct(decimal)
            result_label.config(text=f"Octal: {result}", fg="#00B8D9")
        elif mode == "o2d":
            octal = entry.get()
            result = OctToTen(octal)
            result_label.config(text=f"Decimal: {result}", fg="#00B8D9")
        elif mode == "d2h":
            decimal = int(entry.get())
            result = TenToHex(decimal)
            result_label.config(text=f"Hex: {result}", fg="#00B8D9")
        elif mode == "h2d":
            hexa = entry.get()
            result = HexToTen(hexa)
            result_label.config(text=f"Decimal: {result}", fg="#00B8D9")
    except Exception as e:
        result_label.config(text="Invalid input.", fg="#FF4444")

root = tk.Tk()
root.title("Base Converter")
root.configure(bg="#181A1B")
root.geometry("340x440")
root.resizable(False, False)

var = tk.StringVar(value="b2d")

tk.Label(root, text="Base Converter", font=("Consolas", 18, "bold"), fg="#00B8D9", bg="#181A1B").pack(pady=(18, 2))
tk.Label(root, text="Enter number", font=("Consolas", 12), fg="#E6E6E6", bg="#181A1B").pack(pady=(2, 6))

entry = tk.Entry(root, font=("Consolas", 16), fg="#E6E6E6", bg="#232526", justify="center", width=18, bd=0, relief="flat", insertbackground="#00B8D9")
entry.pack(pady=5, ipady=6)

radio_frame = tk.Frame(root, bg="#181A1B")
radio_frame.pack(pady=(10, 10))

for text, value in [
    ("Binary to Decimal", "b2d"),
    ("Decimal to Binary", "d2b"),
    ("Decimal to Octal", "d2o"),
    ("Octal to Decimal", "o2d"),
    ("Decimal to Hex", "d2h"),
    ("Hex to Decimal", "h2d"),
]:
    tk.Radiobutton(
        radio_frame, text=text, variable=var, value=value,
        font=("Consolas", 11), bg="#181A1B", fg="#E6E6E6",
        selectcolor="#00B8D9", activebackground="#181A1B", activeforeground="#00B8D9",
        highlightthickness=0, bd=0, anchor="w", width=18, pady=2
    ).pack(anchor="w")

tk.Button(
    root, text="Convert", command=convert, font=("Consolas", 13, "bold"),
    bg="#00B8D9", fg="#181A1B", activebackground="#00B8D9", activeforeground="#181A1B",
    padx=10, pady=8, bd=0, relief="flat", cursor="hand2"
).pack(pady=18)

result_label = tk.Label(root, text="", font=("Consolas", 16, "bold"), bg="#181A1B", fg="#00B8D9")
result_label.pack(pady=(5, 10))

entry.focus_set()

root.mainloop()