from twilio.rest import Client
from util import getTime, account_sid, auth_token,addLog

def send(sender,phone,msg):

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
                                    body=msg,
                                    from_=sender,
                                    to=phone
                                )
    except: 
        print('Unable to send')
        return False

    print(f'SMS sent to {phone}')
    print(f"{getTime()} {phone} <= {msg}")
    addLog(sender,phone,msg,"Outgoing")
    return True

