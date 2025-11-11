import datetime
import bday_messages

today = datetime.date.today()
next_birthday = datetime.date(2026, 6, 14)
time_difference = next_birthday - today
days_away = time_difference.days

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {days_away} days away!')
