import csv
from datetime import datetime
from datetime import date
import tkinter as tk
from tkinter import ttk

fileName = "files/days.csv"

dFont = "Calibri"
dPadx = 20
dPady = 12
# entryInput = "yes" #input("Entry? >> ")


today = date.today().strftime("%d-%m-%Y")
now = datetime.now()

class mainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x600")
        self.root.title("Main Window")

        # title
        self.mainLabel = tk.Label(self.root, text="Title Here", font=(dFont, 16))
        
        # text entry
        self.entryBox = tk.Text(self.root)

        # warning label
        self.warning = tk.Label(self.root, text="", font=(dFont, 10))
        
        # submit button
        self.entryButton = tk.Button(self.root, text="Submit Entry", command=lambda: self.writeEntry(otherEntryList))
        
        # view past entries button
        self.viewButton = tk.Button(self.root, text="View Past Entries", command=self.viewEntries)
        
        # pack everything
        self.mainLabel.pack(padx=dPadx, pady=dPady)
        self.entryBox.pack(padx=dPadx, pady=dPady)
        self.warning.pack(padx=dPadx, pady=5)
        self.entryButton.pack(padx=dPadx, pady=dPady)
        self.viewButton.pack(padx=dPadx, pady=dPady)
        self.root.mainloop()
    


    # second text box for viewing past entries
    def viewEntries(self):
        entriesWindow = tk.Toplevel(self.root)
        entryList = readFile(fileName)
        formattedEntries = ""
        for i in entryList:
            formattedEntries = formattedEntries + str(i[0]) + ", " + str(i[1]) + " >> " + str(i[2]) + "\n\n"
        entriesWindow.title("Past Entries")
        entriesWindow.geometry("500x350")

        self.words = tk.Text(entriesWindow,
                              width=50)
        self.words.pack(padx=dPadx, pady=dPady)
        self.words.insert("1.0", formattedEntries)
        self.words.config(state="disabled")
    

    # write to the CSV file
    def writeEntry(self, list_of_entries):
        entryInput = self.entryBox.get("1.0", tk.END)

        if list_of_entries[-1][0] != datetime.today():
            print("today is today")
            if entryInput != "\n":
                with open(fileName, "w", encoding="utf-8", newline="") as fileObjW:
                    w = csv.writer(fileObjW)
                    
                    fullEntry = [str(today),str(now.strftime("%H:%M:%S")),entryInput.replace("\n", "")]
                    list_of_entries.append(fullEntry)
                    for i in list_of_entries:
                        w.writerow(i)
                    
                    fileObjW.close()
            else:
                self.warning.config(text = "There's nothing in the entry box!")
        else:
            self.warning.config(text = "You've already written an entry today. Come back tomorrow?")


# reading file
def readFile(name):
    with open(name, "r", encoding="utf-8") as fileObjR:
        r = csv.reader(fileObjR)
        entryList = []
        for row in r:
            entryList.append(row)
        fileObjR.close()

    
    return entryList

# here you do the thing
otherEntryList = readFile(fileName)
mainWindow()