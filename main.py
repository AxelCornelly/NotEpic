# Clinic Patient Database Project
# Author: Axel Cornelly
# Last Edited: 01/18/2022

# Desc:
# A program similar to Epic, a software in the medical field
# that allows healthcare providers to chart their work
# and retrieve and view patient information.
# DISCLAIMER: ALL PATIENT INFO IN THIS PROJECT IS 
# ARTIFICIAL AND IN NO WAY CORRELATED TO REAL PATIENTS

from msilib.schema import RadioButton
from tkinter.constants import *
import clinicDB as db
import tkinter as tk

# Main window
window = tk.Tk()
window.title("NotEpic")
application = tk.Frame(master=window, width=500, height=500, background="#a5dff8")
application.pack(fill=BOTH, expand=True)

appBottomFrame = tk.Frame(application, background="#a5dff8") # Frame to hold bottom half of start page
appBottomFrame.pack(side=BOTTOM, fill=BOTH, expand=True)

# Application Menues
mainMenu = tk.Menu(window)
mainMenu.add_command(label="Home", command=lambda: returnHome())
mainMenu.add_command(label="Schedule", command=lambda: openPage(scheduleFrame))
mainMenu.add_command(label="Chart", command=lambda: openPage(chartFrame))
mainMenu.add_separator()

# Frame for Schedule screen
scheduleFrame = tk.Frame(window, background="#a5dff8")
scheduleLabel = tk.Label(scheduleFrame, text="A calendar should be here", background="#a5dff8")
scheduleLabel.pack()
scheduleFrame.pack(fill=BOTH, expand=True)
scheduleFrame.place(in_=application, x=0, y=0, relwidth=1, relheight=1)

# Frame for Chart screen
chartFrame = tk.Frame(window, background="#a5dff8")
chartLabel = tk.Label(chartFrame, text="Charting stuff goes here", background="#a5dff8")
chartLabel.pack()
chartFrame.pack(fill=BOTH, expand=True)
chartFrame.place(in_=application, x=0, y=0, relwidth=1, relheight=1)

# Frame for the "Add Patient" screen
addPatientFrame = tk.Frame(window, background="#a5dff8")
addPatientLabel = tk.Label(addPatientFrame, text="Please Enter Patient Information", background="#a5dff8")
addPatientLabel.pack()
addPatientFrame.pack(fill=BOTH, expand=True)

addPatientFrame.place(in_=application, x=0, y=0, relwidth=1, relheight=1)

# "Add Patient" screen widgets and functions

# Variables for entries
idInput = tk.StringVar(application, "ID")
fnameInput = tk.StringVar(application, "First Name")
lnameInput = tk.StringVar(application, "Last Name")
addressInput = tk.StringVar(application, "Address")
providerIdInput = tk.StringVar(application, "Provider ID")
birthdateInput = tk.StringVar(application, "Birthdate (YYYY/MM/DD)")
ageInput = tk.StringVar(application, "Age")
commentsInput = tk.StringVar(application, "Comments")
submissionVar = tk.StringVar(application, "")

idEntry = tk.Entry(addPatientFrame, textvariable=idInput)
idEntry.bind('<Button-1>', lambda e: idEntry.delete(0, END)) # click event to clear entry
idEntry.pack()
fNameEntry = tk.Entry(addPatientFrame, textvariable=fnameInput)
fNameEntry.bind('<Button-1>', lambda e: fNameEntry.delete(0, END)) 
fNameEntry.pack()
lNameEntry = tk.Entry(addPatientFrame, textvariable=lnameInput)
lNameEntry.bind('<Button-1>', lambda e: lNameEntry.delete(0, END)) 
lNameEntry.pack()
addressEntry = tk.Entry(addPatientFrame, textvariable=addressInput)
addressEntry.bind('<Button-1>', lambda e: addressEntry.delete(0, END)) 
addressEntry.pack()
providerEntry = tk.Entry(addPatientFrame, textvariable=providerIdInput)
providerEntry.bind('<Button-1>', lambda e: providerEntry.delete(0, END)) 
providerEntry.pack()
birthdateEntry = tk.Entry(addPatientFrame, textvariable=birthdateInput)
birthdateEntry.bind('<Button-1>', lambda e: birthdateEntry.delete(0, END)) 
birthdateEntry.pack()
ageEntry = tk.Entry(addPatientFrame, textvariable=ageInput)
ageEntry.bind('<Button-1>', lambda e: ageEntry.delete(0, END)) 
ageEntry.pack()
commentEntry = tk.Entry(addPatientFrame, textvariable=commentsInput)
commentEntry.bind('<Button-1>', lambda e: commentEntry.delete(0, END)) 
commentEntry.pack()

# Function to parse patient info entered
def parseInfo():
    # First retrieve and store all information
    info = []
    for value in (idEntry,fNameEntry,lNameEntry,addressEntry,providerEntry,birthdateEntry,ageEntry,commentEntry):
        info.append(value.get())
    
    insertQuery = "INSERT INTO patient VALUES (%s, \"%s\", \"%s\", \"%s\", %s, \"%s\", %s, \"%s\")" % (info[0], info[1], info[2], info[3], info[4], info[5], info[6], info[7])
    try:
        db.cursor.execute(insertQuery)
    except:
        submissionVar.set("Error: Couldn't Add Patient")
    else:
        db.clinicDB.commit() # committing query to save data to database
        submissionVar.set("Patient added!")
    addPatientFrame.focus()



submissionStatus = tk.Label(addPatientFrame, textvariable=submissionVar, background="#a5dff8")
submissionStatus.pack()
submitPatientButton = tk.Button(addPatientFrame, text="Submit", command=parseInfo)
submitPatientButton.pack()

homeButton = tk.Button(addPatientFrame, text="Back", command= lambda: returnHome())
homeButton.pack()

# Functions to open diffw
def openPage(page):
    page.lift()

# Similar function as openPage but strictly for home page
def returnHome():
    application.lift()
    db.cursor.execute("SELECT * FROM patient")
    info = ""
    for record in db.cursor:
        info += (" | ".join(map(str, record)) + "\n")

    patientInfo.set(info)


# Bridge function to utilize correct search method
def searchPatient(option):
    if option.get() == "byName":
        searchByName()
    elif option.get() == "byID":
        searchByID()
    elif option.get() == "byProviderID":
        searchByProviderID()
    
    searchVar.set("Search")

# Function for patient search by name
def searchByName():
    content = searchVar.get() # Reading Entry widget value
    name = content.split(" ") # Parsing data
    result = "" # Variable to change textvariable later

    # Checking for correct input length (Length of 2 for first and last name; middle name excluded)
    if len(name) == 0:
        application.focus()
        return
    elif len(name) > 2:
        result = "Invalid input!"
        patientInfo.set(result)
        application.focus()
        return

    # Split data into 2 holder variables for first and last name
    fname = name[0]
    lname = name[1]
    # Executing SQL query 
    searchQuery = "SELECT * FROM patient WHERE f_name = \"%s\" AND l_name = \"%s\"" % (fname, lname)
    db.cursor.execute(searchQuery)
    queryResult = db.cursor.fetchall()

    if len(queryResult) == 0: # Case for no results
        result = "No patients found."
    else:
        for item in queryResult:
            result += (" | ".join(map(str, item)) + "\n")

    patientInfo.set(result)
    searchVar.set("Search")
    application.focus()

def searchByID():
    input = searchVar.get() # Grabbing user input, should be a positive integer
    query = "SELECT * FROM patient WHERE id= %s" % (input)
    result = ""

    try:
        db.cursor.execute(query)
        queryResult = db.cursor.fetchall()
    except:
        patientInfo.set("Unable to search for patient.")
    else:
        if(len(queryResult) == 0):
            patientInfo.set("No patients found.")
        else:
            for item in queryResult:
                result += (" | ".join(map(str, item)))
            patientInfo.set(result)
    
    application.focus()

def searchByProviderID():
    # do stuff here
    application.focus()

# Search Bar and functionality
searchVar = tk.StringVar(application, "Search")
searchBar = tk.Entry(master=application, width=20, textvariable=searchVar)
searchBar.pack()
searchBar.bind('<Button-1>', lambda e: searchBar.delete(0, END)) # click event to clear search bar

# Search Button
searchButton = tk.Button(master=application,text="Search",command= lambda: searchPatient(searchOption))
searchButton.pack()

# Frame for search options
searchOptionFrame = tk.Frame(application, background="#a5dff8")
searchOptionFrame.pack(expand=True)

# Different Search Options
searchOption = tk.StringVar()
byName = tk.Radiobutton(searchOptionFrame, bg="#a5dff8", text="By Name", variable=searchOption, value="byName")
byName.pack(side=LEFT)
byID = tk.Radiobutton(searchOptionFrame, bg="#a5dff8", text="By ID", variable=searchOption, value="byID")
byID.pack(side=LEFT)
byProviderID = tk.Radiobutton(searchOptionFrame, bg="#a5dff8", text="By Provider ID", variable=searchOption, value="byProviderID")
byProviderID.pack(side=LEFT)

byName.select() # default 

# Add patient button
addPatientButton = tk.Button(application,text="Add Patient", command= lambda: openPage(addPatientFrame))
addPatientButton.pack(side=BOTTOM)

patientTableColumns = tk.Label(appBottomFrame, text="ID | FName | LName | Address | Provider | Birthdate | Age | Comments", width=125, background="#a5dff8")
patientTableColumns.pack(side=TOP, fill=X, expand = True)

patientInfo = tk.StringVar()
patientRecord = tk.Label(appBottomFrame, textvariable=patientInfo, background="#a5dff8")
patientRecord.pack(side=BOTTOM, fill=X, expand=True)

# Display all records on startup
returnHome()

window.config(menu=mainMenu)
application.mainloop()