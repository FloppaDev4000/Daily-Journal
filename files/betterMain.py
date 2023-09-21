import csv
import datetime

fileName = "days.csv"

entryInput = input("Entry? >> ")

today = str(datetime.date.today())
print(today) #edit out later

# reading file
with open(fileName, "r", encoding="utf-8") as fileObjR:
    r = csv.reader(fileObjR)
    doneToday = today == r[-1][0]

# here compare today w/ most recent entry
if doneToday:
    # replace recent entry w/ new thing
    print("Replaced.")
else:
    # append list w/ new entry
    print("Appended.")

viewInput = input("View? >>")
if viewInput == "Y":
    # print recent entries (or all)
    pass #edit out later