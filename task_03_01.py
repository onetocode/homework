import datetime

def get_days_to_new_year():
    today = datetime.date.today()
    newyear = datetime.date(today.year + 1, 1, 1)
    delta = newyear - today
    return delta.days