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
