# twilio_messager

Twilio Messager is a python programme that sends and receives SMS using SMS-enabled Twilio phone numbers.

<!-- GETTING STARTED -->

## Getting Started

Follow these steps to use this application locally.

### Install Dependencies

- Install twilio
  ```
  pip install twilio
  ```
- Install flask
  ```
  pip install -U Flask
  ```

### Set Account SID and Auth Token

1. Go to [Twilio console](https://www.twilio.com/console) to get your credentials

   ![get-credentials](/img/get_credentials.png)

2. Replace `YOUR_ACCOUND_SID` and `YOUR_AUTH_TOKEN` in `util.py` with your own credentials

### Connect Twilio to Your App

1. [Download ngrok](https://ngrok.com/download) and [Sign up for a free account](https://dashboard.ngrok.com/signup)

2. Go to ngrok dashboard to get your authtoken

   ![get-authtoken](/img/ngrok_authtoken.png)

3. Open a terminal in the directory of Ngrok excutable and type

   ```
   ngrok authtoken YOUR_NGROK_AUTHTOKEN
   ```

   Replace `YOUR_NGROK_AUTHTOKEN` with your own ngrok authtoken. You only need to do this once.

4. Start ngrok
   ```
   ngrok http 5000
   ```
   You will see the ngrok console UI once it starts.
5. Add `/sms` to your ngrok HTTP forwarding URL. Then set it to the webhook address of your number(s) on [Twilio console](https://www.twilio.com/console)

   ```
   http://example.ngrok.io/sms
   ```

   ![set-webhook](/img/set_webhook.png)

## Usage

Run the `main.py` script to start the messager

```
python main.py
```

### Phone Number

Enter phone number starting with `+COUNTRY_CODE`
You may lookup your country code [here](https://countrycode.org/)

### Cancel

Add `$` to the end of a message or phone number to cancel operation

![cancel](/img/cancel.png)

### Log File

A log file `Instance.csv` will be automatically if there is no such file in the programme directory. It stores messaging data in the format of `Timestamp,Sender,Receiver,Message,Type`
If there is already an `Instance.csv` in the programme directory, new logs will be appended to the existing log file.

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<!-- CONTACT -->

## Contact

Songyue Wang Aaron - me@songyue.wang

Project Link: [https://github.com/songyuew/twilio_messager](https://github.com/songyuew/twilio_messager)

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

- [Ngrok Docs](https://ngrok.com/docs)
- [Twilio Docs](https://www.twilio.com/docs)
- [CountryCode](https://countrycode.org/)
