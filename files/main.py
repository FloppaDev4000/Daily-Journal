# author:		Adam Noonan
# date:			20/09/2023
# last-updated:	20/09/2023
# purpose:		check if entry has been written today.

# TO DO:
# add time of entry to record
# come up with use for programme
# make GUI

# importing stuff
from datetime import date
import csv

# variables
today = str(date.today())

doneToday = False
willWrite = False

fileName = "days.csv"

# reading file
with open(fileName, "r", encoding="utf-8") as fileObjR:
    r = csv.reader(fileObjR)
    for row in r:
        if row[0] == today:
            doneToday = True
            print("Today is done already. You said: \"" + row[1] + "\".")
            break
    fileObjR.close()

# check if we can write today
if not doneToday:
    print("Not done yet!")
    doneToday = True
    willWrite = True

# writing to file
if willWrite:
    with open(fileName, "w", encoding="utf-8") as fileObjW:
        w = csv.writer(fileObjW)
        entryWords = input("Entry >> ")
        fullEntry = [today, entryWords]
        w.writerow(fullEntry)
        
        fileObjW.close()
    