# Clinic Patient Database Project
# Author: Axel Cornelly
# Last Edited: 01/08/2022

# Desc:
# A program similar to Epic, a software in the medical field
# that allows healthcare providers to chart their work
# and retrieve and view patient information.
# DISCLAIMER: ALL PATIENT INFO IN THIS PROJECT IS 
# ARTIFICIAL AND IN NO WAY CORRELATED TO REAL PATIENTS

import mysql.connector

#Initializing and connecting to MySQL
clinicDB = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "epic_clone_project"
)
#print(bookDB)

#cursor to execute sql queries
cursor = clinicDB.cursor()

