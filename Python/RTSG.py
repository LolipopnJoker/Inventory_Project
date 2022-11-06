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

def random_timestamp_generator(opening_hour, opening_minute, opnening_second, closing_hour, closing_minute, closing_second):

    random_hour = random.randint(opening_hour, closing_hour)
    if random_hour == opening_hour:
        random_minute = random.randint(opening_minute, 59)
        random_second = random.randint(opnening_second, 59)
    elif random_hour == closing_hour:
        random_minute = random.randint(0, closing_minute)
        random_second = random.randint(0, closing_second)
    else:
        random_minute = random.randint(0, 59)
        random_second = random.randint(0, 59) 
    
    random_timestamp = datetime.time(random_hour, random_minute, random_second)

    return random_timestamp

print(random_timestamp_generator(9, 0, 0, 22, 30, 0))
