def send_email(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                  .execute())
        print('Message Id: %s' % message['id'])
        return message
    except Exception as error:
        # Call to the error handling tool (yet to be implemented)
        handle_api_error(error)
        return None