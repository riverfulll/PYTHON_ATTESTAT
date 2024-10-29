from datetime import datetime

def date_time():
    now = datetime.now()
    final = now.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = now.strftime('%A')
    numb_week = now.isocalendar()[1]

    print(f'Current date and time: {final}')
    print(f'Day of the week: {day_of_week}')
    print(f'Week number: {numb_week}')


if __name__ == '__main__':
    date_time()