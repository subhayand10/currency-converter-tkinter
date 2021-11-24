from tkinter import *
from tkinter.ttk import Combobox
from google_currency import convert
import json
from tkinter import messagebox

root = Tk()
root.geometry("600x400")
root.title("Subhayan Currency Convertor")
root.iconbitmap("dollar.ico")
root.config(bg="lightblue")

with open("ind.txt") as f:
    lines = f.readlines()

dictop = {}    
for line in lines:
    opaq = line.split("\t")
    dictop[opaq[1]] =  opaq[2]

def functionbutton():
    try:
        lightbox = Combobox1.get()
        heavybox = Combobox2.get()
        lapto = dictop[lightbox]
        lapti = dictop[heavybox]
        serial = var1.get() 
        opol = convert(lapto, lapti, serial)
        lope = json.loads(opol)
        jsonfix = lope["amount"]
        var2.set(jsonfix)
    except:
        rr = messagebox.askretrycancel("A Problem Has Been Occured", "Please Check your Internet Connection or Check the Amount You Have Entered.")

Title = Label(root, text="Subhayan Currency Convertor", fg="green",  bg="lightblue", font=("ubuntu", 15, "italic"))
Title.place(x=170, y=10)

Label1 = Label(root, text="Enter the Amount to Convert :- ", bg="lightblue", fg="brown", font=("ubuntu", 15, "bold"))
Label1.place(x=15, y=60)

var1 = IntVar()
feeder = Entry(root, width=24 ,text=var1, bg="grey", fg="yellow", font=("ubuntu", 15, "bold"))
feeder.place(x=320, y=60)

Label2 = Label(root, text="Select the Currency to Convert Your Amount From :- ", bg="lightblue", fg="orange", font=("ubuntu", 10, "bold"))
Label2.place(x=15, y=120)

slider = StringVar()
Combobox1 = Combobox(root, width=30, textvariable=slider, state="readonly", font=("ubuntu", 10, "bold"))
Combobox1['values'] = [item for item in dictop.keys()]
Combobox1.current(4)
Combobox1.place(x=350, y=120)

Lable3 = Label(root, text="Select the Currency to Convert Your Amount To :-  ", bg="lightblue", fg="orange", font=("ubuntu", 10, "bold"))
Lable3.place(x=15, y=160)

foreground = StringVar()
Combobox2 = Combobox(root, width=30, textvariable=foreground, state="readonly", font=("ubuntu", 10, "bold"))
Combobox2['values'] = [item for item in dictop.keys()]
Combobox2.current(0)
Combobox2.place(x=350, y=160)

Button1 = Button(root, bg="lightgreen", text="Convert", command=functionbutton , fg="grey", font=("ubuntu", 15, "bold"), relief=RAISED,\
                            cursor="hand2")
Button1.place(x=240, y=220)

Label4 = Label(root, text="Converted Amount Here :- ", bg="lightblue", fg="brown", font=("ubuntu", 15, "bold"))
Label4.place(x=15, y=280)

var2 = IntVar()
Entry2 = Entry(root, textvariable=var2, fg="blue", state="readonly",width=27, font=("ubuntu", 15, "bold"))
Entry2.place(x=280, y=280)

footer = Label(root, text="Developed and Designed By Subhayan Das",bg="lightblue", fg="grey", font=("ubuntu", 15, "bold"))
footer.place(x=100, y=340)


root.mainloop()