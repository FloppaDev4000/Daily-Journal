# Author:       Adam Noonan

import csv
from datetime import datetime
from datetime import date
import tkinter as tk
from tkinter import ttk

# TO DO:
#   find a reason for this thing to exist
#   put window variables in a separate place to make it easier to edit
#   add comments
#   figure out why i need 2 read file functions

fileName = "files/days.csv"

# default tkinter variables
dFont = "Calibri"
dPadx = 20
dPady = 12

#get current time
today = date.today().strftime("%d-%m-%Y")
now = datetime.now()

# main app window
class mainWindow:
    def __init__(self):

        #initialize window
        self.root = tk.Tk()
        self.root.geometry("500x600")
        self.root.title("Journal")

        # title
        self.mainLabel = tk.Label(self.root, text="Submit your entry below!", font=(dFont, 16))
        
        # text entry
        self.entryBox = tk.Text(self.root)

        # warning label
        self.warning = tk.Label(self.root, text="", font=(dFont, 10))
        
        # submit button
        self.entryButton = tk.Button(self.root, text="Submit Entry", command=lambda: self.writeEntry(otherEntryList))
        
        # view past entries button
        self.viewButton = tk.Button(self.root, text="View Past Entries", command=self.viewEntries)
        
        # pack everything up on the window
        self.mainLabel.pack(padx=dPadx, pady=dPady)
        self.entryBox.pack(padx=dPadx, pady=dPady)
        self.warning.pack(padx=dPadx, pady=5)
        self.entryButton.pack(padx=dPadx, pady=dPady)
        self.viewButton.pack(padx=dPadx, pady=dPady)
        self.root.mainloop()
    


    # second text box for viewing past entries
    def viewEntries(self):

        # processing the list of past entries
        entriesWindow = tk.Toplevel(self.root)
        entryList = readFile(fileName)
        entryList.reverse()
        formattedEntries = ""
        for i in entryList:
            formattedEntries = formattedEntries + str(i[0]) + ", " + str(i[1]) + " >> " + str(i[2]) + "\n\n"
        entriesWindow.title("Past Entries")
        entriesWindow.geometry("600x350")

        # displaying the list of past entries
        self.words = tk.Text(entriesWindow,
                              width=100)
        self.words.pack(padx=dPadx, pady=dPady)
        self.words.insert("1.0", formattedEntries)
        self.words.config(state="disabled")
    

    # write to the CSV file. Only allowed if text box has stuff in it + no entries written today
    def writeEntry(self, list_of_entries):
        entryInput = self.entryBox.get("1.0", tk.END)

        if list_of_entries[-1][0] != today:
            if entryInput != "\n":
                self.warning.config(text = "Submitted!")
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

# start the programme
otherEntryList = readFile(fileName)
mainWindow()