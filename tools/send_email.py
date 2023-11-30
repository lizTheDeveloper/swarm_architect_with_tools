from googleapiclient.discovery import build
import base64

def send_email(sender_email, recipient_email, subject, message_text):
    service = build('gmail', 'v1', credentials=credentials)
    encoded_email = create_email_message(sender_email, recipient_email, subject, message_text)
    
    try:
        # Create a message object using the encoded email
        message = {'raw': encoded_email}
        # Use the Gmail API to send the email
        sent_message = service.users().messages().send(userId='me', body=message).execute()
        return sent_message['id']
    except Exception as e:
        # A more sophisticated error handling might be desired
        print(f'An error occurred: {e}')
        return None
    
from email.mime.text import MIMEText
import base64


def create_email_message(sender_email, recipient_email, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = recipient_email
    message['from'] = sender_email
    message['subject'] = subject
    
    # Base64 encode the bytes-like object.
    encoded_email = base64.urlsafe_b64encode(message.as_bytes()).decode()
    
    return encoded_email

tool_definition = {
    "name": "send_email",
    "description": "Send an email message",
    "parameters": {
        "type": "object",
        "properties": {
        "to_email": {
            "type": "string",
            "description": "The email address to send the message to"
        },
        "subject": {
            "type": "string",
            "description": "The subject of the message"
        },
        "message_body": {
            "type": "string",
            "description": "The body of the message to send"
        }
        },
        "required": [
        "to_email",
        "subject",
        "message_body"
        ]
    }
    }