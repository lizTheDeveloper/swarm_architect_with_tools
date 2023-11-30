# Python code placeholder for Twilio SMS Sender tool
import os
from twilio.rest import Client

def send_sms(to_number, message_body):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    from_number = os.getenv('TWILIO_SMS_NUMBER') # Set your Twilio SMS number in environment variables
    message = client.messages.create(
      to=to_number, 
      from_=from_number,
      body=message_body
    )

    return {'status': 'Success', 'message_sid': message.sid}
  
  
tool_definition = {
  "name": "send_sms",
  "description": "Send an SMS message to a phone number",
  "parameters": {
    "type": "object",
    "properties": {
      "to_number": {
        "type": "string",
        "description": "The phone number to send the message to"
      },
      "message_body": {
        "type": "string",
        "description": "The body of the message to send"
      }
    },
    "required": [
      "to_number",
      "message_body"
    ]
  }
}