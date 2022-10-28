#Imports
import random
import datetime


def random_date_generator(start_year: int, start_month: int, start_day: int, end_year: int, end_month: int, end_day: int):
    
    start_date = datetime.date(start_year, start_month, start_day)
    end_date = datetime.date(end_year, end_month, end_day)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    return random_date
"""
def random_timestamp_generator(opening_hour, opening_minute, opnening_second, closing_hour, closing_minute, closing_second):
    
    opening_time = datetime.time(opening_hour, opening_minute, opnening_second)
    closing_time = datetime.time(closing_hour, closing_minute, closing_second)

    opreation_time = closing_time - opening_time

    print(opreation_time)

random_timestamp_generator(9, 0, 0, 21, 30, 0)
"""