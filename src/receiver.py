from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from util import getTime, account_sid, auth_token, addLog

client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms_reply():

    resp = MessagingResponse()
    print()
    incomingNumber = request.values.get('From',None)
    receiverNumber = request.values.get('To',None)

    msg = request.values.get("Body",None)
    print(f"SMS received on {receiverNumber}")
    print(f"{getTime()} {incomingNumber} => {msg}")
    
    addLog(incomingNumber,receiverNumber,msg,"Incoming")

    return str(resp)
