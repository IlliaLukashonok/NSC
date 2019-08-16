from tkinter import *
from Converters import *

VERSION = 2.0

root = Tk()

def input_val(dec, bin, hex):
    """ Inserts specified value into text widget """
    output_dec.config(state=NORMAL)
    output_bin.config(state=NORMAL)
    output_hex.config(state=NORMAL)
    output_dec.delete("0","end")
    output_dec.insert("0",dec)
    output_bin.delete("0","end")
    output_bin.insert("0",bin)
    output_hex.delete("0","end")
    output_hex.insert("0",hex)
    output_dec.config(state="readonly")
    output_bin.config(state="readonly")
    output_hex.config(state="readonly")

def clear(event):
    """ Clears entry form """
    caller = input_dec
    caller.delete("0", "end")
    caller = input_bin
    caller.delete("0", "end")
    caller = input_hex
    caller.delete("0", "end")

def convert():
    if input_dec.get() != '' and\
       input_hex.get() == '' and\
       input_bin.get() == '':
        if input_dec.get().isdigit() is True:
            input_val(
                input_dec.get(),
                converter_from_dec(input_dec.get(), 2),
                converter_from_dec(input_dec.get(), 16))
        else:
            input_val(
                "Enter correct number",
                "Enter correct number",
                "Enter correct number")
    elif input_bin.get() != '' and\
         input_dec.get() == '' and\
         input_hex.get() == '':
        input_val(
            converter_to_dec(input_bin.get(), 2),
            input_bin.get(),
            converter_bin_to_hex(input_bin.get()))
    elif input_hex.get() != '' and\
         input_bin.get() == '' and\
         input_dec.get() == '':
        input_val(
            converter_to_dec(input_hex.get(), 16),
            converter_hex_bin(input_hex.get()),
            input_hex.get())

frame1 = Frame(root, bd=2)
frame1.pack(side=LEFT, fill=Y)
frame2 = Frame(root, bd=2)
frame2.pack(side=RIGHT, fill=Y)

# Inputs in 1 frame.
lab_dec = Label(frame1, text="dec")
lab_dec.pack(side=TOP, pady=(70, 0))

input_dec = Entry(frame1, width=40, justify=CENTER)
input_dec.insert(0, "dec")
input_dec.bind("<FocusIn>", clear)
input_dec.bind("<Return>", lambda event: convert())
input_dec.pack(side=TOP, pady=(0, 80))

lab_bin = Label(frame1, text="bin")
lab_bin.pack(side=TOP)

input_bin = Entry(frame1, width=40, justify=CENTER)
input_bin.insert(0, "bin")
input_bin.bind("<FocusIn>", clear)
input_bin.bind("<Return>", lambda event: convert())
input_bin.pack(side=TOP, pady=(0, 80))

lab_hex = Label(frame1, text="hex")
lab_hex.pack(side=TOP)

input_hex = Entry(frame1, width=40, justify=CENTER)
input_hex.insert(0, "hex")
input_hex.bind("<FocusIn>", clear)
input_hex.bind("<Return>", lambda event: convert())
input_hex.pack(side=TOP)

# Convert button.
btn_conv = Button(root, text="Convert", command=convert)
btn_conv.pack(expand=1)

# Labels in 2 frame.
lab2_dec = Label(frame2, text="dec")
lab2_dec.pack(side=TOP, pady=(70, 0))

output_dec = Entry(frame2, width=40, state="readonly", justify=CENTER)
output_dec.insert(0, "dec")
output_dec.pack(side=TOP, pady=(0, 80))

lab2_bin = Label(frame2, text="bin")
lab2_bin.pack(side=TOP)

output_bin = Entry(frame2, width=40, state="readonly", justify=CENTER)
output_bin.insert(0, "bin")
output_bin.pack(side=TOP, pady=(0, 80))

lab2_hex = Label(frame2, text="hex")
lab2_hex.pack(side=TOP)

output_hex = Entry(frame2, width=40, state="readonly", justify=CENTER)
output_hex.insert(0, "hex")
output_hex.pack(side=TOP)

root.title("Numeral Systems Converter")
root.geometry("640x480+200+300")
root.resizable(False, False)

root.mainloop()
