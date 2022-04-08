import datetime
import csv

'''
Replace YOUR_ACCOUNT_SID and YOUR_AUTH_TOKEN with your own credentials
'''
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

def getTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def addLog(sender,receiver,msg,type):
    with open('Instance.csv', 'a+', newline="")as file:
            csvWriter = csv.writer(file) 
            csvWriter.writerow([getTime(),sender,receiver,msg,type])