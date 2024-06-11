import datetime

def add_working_days(start_date, working_days):
    # start_date = datetime.date.today()
    current_date = start_date
    while working_days > 0:
        current_date += datetime.timedelta(days=1)
        # Check if the current day is a weekday (Monday to Friday)
        if current_date.weekday() < 5:  # Monday is 0 and Friday is 4
            working_days -= 1
    return current_date