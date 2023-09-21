import tkinter as tk

dFont = "Calibri"

class myGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text="Entry", font=(dFont, 16))
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5, font=(dFont, 15))
        self.textbox.pack(padx=10, pady=10)

        self.check_state = tk.IntVar
        
        self.check = tk.Checkbutton(self.root, text="Messagebox check", font=(dFont, 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=(dFont, 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        print("YES")

myGUI()

'''
root = tk.Tk()

root.geometry("500x500")
root.title("window 1")

label = tk.Label(root, text="Write your Entry", font=(dFont, 18))
label.pack(padx = 20, pady = 20)

entryBox = tk.Text(root, height=5, width=40, font=(dFont, 14))
entryBox.pack(padx = 20)

entryButton = tk.Button(root, text="enter", font=(dFont, 18))
entryButton.pack(padx = 30, pady = 10)

viewButton = tk.Button(root, text="click to view past entries", font=(dFont, 15))
viewButton.pack(padx = 30, pady = 10)

root.mainloop()
'''