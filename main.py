from twilio.rest import Client
from datetime import datetime

import time

account_SID = ''
auth_token = ''

client = Client(account_SID, auth_token)

def send_message(number, message_body):
    try : 
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body= message_body,
            to=f'whatsapp:{number}'
        )
        print(f'Message sent succefully! message ID is : {message.sid}')
    except Exception as e :
        print(e)

name = input("Enter name :")
numberTo = input("Enter whatsapp number with country code :")
message = input(f"Enter message you want to send to {name} :")

date_Str = input('Enter date you want to send at : (YYYY-MM-DD)')
time_Str = input('Enter time you want to send at : (HH-MM) in 24 Hr')

sheduled_date = datetime.strptime(f'{date_Str} {time_Str}', '%Y-%m-%d %H:%M')
current_date = datetime.now()

time_diff = sheduled_date - current_date
delay_Sec = time_diff.total_seconds()

if delay_Sec <= 0:
    print("Message can's be send in past, enter future date and time.")
else :
    print(f'message sheduled to send.')
    time.sleep(delay_Sec)
    send_message(numberTo, message)