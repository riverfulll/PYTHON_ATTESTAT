from datetime import datetime, timedelta


def future_date(days_from_now):
    today = datetime.now()
    future_date = today + timedelta(days=days_from_now)
    final_future_date = future_date.strftime('%Y-%m-%d')
    return final_future_date


if __name__ == '__main__':
    days = 47
    print(f'Date {days} days from now: {future_date(days)}')