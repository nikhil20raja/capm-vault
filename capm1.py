import tkinter


def get_value(entryWidget):
    value = entryWidget.get()
    try:
        return int(value)
    except ValueError:
        return None

def convert(e1, e2, e3):
    if e1 is None or e2 is None or e3 is None:
        return None
    else:
        return e2+(e1*(e3-e2))

def set_label_text(label, entry1, entry2, entry3):
    value = convert(get_value(entry1), get_value(entry2), get_value(entry3))
    if value is None:
        label['text'] = "Enter values for Beta, Risk-Free Rate, Expected Market Return"
    else:
        label['text'] = "Expected Return: " + str(value) + "%"


root = tkinter.Tk()
root.geometry("400x150")
root.title("CAPM Calculator")

frame = tkinter.Frame(root)
frame.pack() 

e1 = tkinter.Entry(frame, width = 15)
e1.insert(1, 'Beta')

e2 = tkinter.Entry(frame, width = 15)
e2.insert(0, 'Risk-Free Rate')

e3 = tkinter.Entry(frame, width = 15)  
e3.insert(0, 'Exp. Market Return')

l = tkinter.Label(root, text="Insert Values as Percentages")
b = tkinter.Button(root, text="Calculate", command=lambda: set_label_text(l, e1, e2, e3))

e1.pack()
e2.pack()
e3.pack()
l.pack()
b.pack()

root.mainloop()