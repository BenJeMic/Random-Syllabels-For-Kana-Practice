import tkinter as tk
import random as rndm
import sylData

root = tk.Tk()
root.geometry("500x200")
root.title("Syllabel Generator")

display = tk.StringVar()
headerTitle = tk.Label(root, text="Syllabel Generator", font=(16)).pack()
tk.Entry(root, state="readonly", textvariable=display, justify="center").pack(fill="x") #Display for showing the result

#Making checkbutton and corresponding data point
check_buttons = [tk.IntVar() for _ in range(15)]
syllable_data = [sylData.first, sylData.kaiueo, sylData.saiueo, sylData.taiueo, sylData.naiueo,
                 sylData.haiueo, sylData.maiueo, sylData.yaiueo, sylData.raiueo, sylData.gaiueo,
                 sylData.zaiueo, sylData.daiueo, sylData.baiueo, sylData.paiueo, sylData.special]

#Configure inputContainer
inputContainer = tk.Frame(root)
for i in range(5):
    inputContainer.columnconfigure(i, weight=1)
inputContainer.pack(fill="x", padx=(20,0))

#Buttons
Buttons = [("AIUEO", check_buttons[0], 0, 0),("K", check_buttons[1], 0, 1),("S", check_buttons[2], 0, 2), ("T", check_buttons[3], 0, 3), ("N",check_buttons[4], 0, 4),
           ("H", check_buttons[5], 1, 0), ("M", check_buttons[6], 1, 1),("Y", check_buttons[7], 1, 2),("R", check_buttons[8], 1, 3), ("G", check_buttons[9], 1, 4),
           ("Z", check_buttons[10], 2, 0), ("D", check_buttons[11], 2, 1), ("B", check_buttons[12], 2, 2), ("P", check_buttons[13], 2, 3), ("Special", check_buttons[14], 2, 4)]
for title, variable, row, column in Buttons:
    tk.Checkbutton(inputContainer, text = title, variable = variable, onvalue=1, offvalue=0, height=2, width=10, anchor="w").grid(row=row, column=column, sticky=tk.W+tk.E)

#Define Generate
def generateText():
    store = []
    for i, data in enumerate(syllable_data):
        if check_buttons[i].get() == 1:
            store.extend(data)
    store2 = ""
    i = 0
    while i <= entryContent.get():
        store2 += " " + store[rndm.randint(0, len(store)-1)]
        i += 1

    display.set(store2)

#Make Generate Section
generateContainer = tk.Frame(root)
generateContainer.columnconfigure(0, weight=1)
generateContainer.columnconfigure(1, weight=1)
generateContainer.pack(fill="x")
def validate_input(P):
    # Check if P is a digit or an empty string
    return P.isdigit() or P == ""
entryContent = tk.IntVar()
entry = tk.Entry(generateContainer,text = "Amount:",textvariable=entryContent, validate="key", validatecommand=(root.register(validate_input), "%P")).grid(column=0)
tk.Button(generateContainer, text = "Generate", command= generateText).grid(row=0,column=1)

root.mainloop()