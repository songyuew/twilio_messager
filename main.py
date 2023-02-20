from receiver import app
from sender import send
from threading import Thread
from twilio.rest import Client
from util import getTime, addLog, account_sid, auth_token
import csv
import time
import os

availableNumber = []
numberInUse = []

def switchNumber():
    print("Available numbers:")
    for index, number in enumerate(availableNumber):
        print(f"{index} - {number}\n")
    switch = input("Select a number: ")
    if switch.isdigit() == False:
        print("Invalid input")
        return
    switch = int(switch)
    if switch not in range(0,len(availableNumber)):
        print("Invalid input")
        return
    del numberInUse[0]
    numberInUse.append(availableNumber[switch])
    print(f"Sender number changed to {numberInUse[0]}")

def getActiveNumber():
    client = Client(account_sid, auth_token)
    incoming_phone_numbers = client.incoming_phone_numbers.list(limit=20)
    for record in incoming_phone_numbers:
        if record.capabilities["sms"] == True:
            availableNumber.append(record.phone_number)
    if len(availableNumber) == 0:
        print("No phone number available for SMS")
        print("Instance exited")
        exit()
    else:
        numberInUse.append(availableNumber[0])


def createFile():
    if ("Instance.csv" not in os.listdir()):
        with open('Instance.csv', 'w')as file:
            csvWriter = csv.writer(file) 
            csvWriter.writerow(["Timestamp","Sender","Receiver","Message","Type"])
        print(f"{getTime()} Log file created")

def getLastLineCSV():
    with open('Instance.csv', 'r')as file:
        csvReader = csv.reader(file) 
        lineList = []
        for line in csvReader:
            if line != []: lineList.append(line)
        return lineList[-1]

def newMessage():
    number = input("Enter phone number (start with '+', type '$' to cancel): ")
    if number[-1] == "$":
        print("Cancelled")
        return
    elif (number[0] != "+" or number[1:].isdigit() == False):
        print("Invalid phone number")
        return
    else:
        editMessage(number,"new")

def editMessage(phone,type):
    if type == "new":
        msg = input(f"Send to {phone} (type '$' to cancel): ")
    elif type == "reply":
        msg = input(f"Reply to {phone} (type '$' to cancel): ")
    if msg[-1] == '$':
        print("Cancelled")
        return
    send(numberInUse[0],phone,msg)

    

def mainMenu():
    print(f"Current number in use: {numberInUse[0]}")
    if (getLastLineCSV()[4] == "Incoming"):
        print("1 - New Message")
        print(f"2 - Reply to {getLastLineCSV()[1]}")
        replyNumber = getLastLineCSV()[1]
        print(f"3 - Switch Number")
        print("4 - Exit")
        sel = input("Select an option [1/2/3/4]: ")
        if (sel not in ["1","2","3","4"]):
            print("Invalid input")
            mainMenu()
        else:
            if sel == "1":
                newMessage()
            elif sel == "2":
                editMessage(replyNumber, "reply")
            elif sel == "2":
                switchNumber()
            elif sel == "4":
                print("Instance exited")
                exit()
    elif (getLastLineCSV()[4] != "Incoming"):
        print("1 - New Message")
        print("2 - Switch Number")
        print("3 - Exit")
        sel = input("Select an option [1/2/3]: ")
        if (sel not in ["1","2","3"]):
            print("Invalid input")
            mainMenu()
        else:
            if sel == "1":
                newMessage()
            if sel == "2":
                switchNumber()
            elif sel == "3":
                print("Instance exited")
                os._exit(0)

def receiving():
    app.run(debug=False)

def takeInput():
    while True:
       mainMenu()

if __name__ == '__main__':
    getActiveNumber()
    createFile()
    print(f"{getTime()} New instance started")
    Thread(target = receiving).start()
    time.sleep(2)
    Thread(target = takeInput).start()