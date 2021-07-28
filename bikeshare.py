import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks users to specify city, month and day to analyze
    """

    print('Hello! Let\'s explore the US bikeshare data!')
    city = input('What city data you would like to explore? Chicago, New York or Washington! ').title()
    while city not in (CITY_DATA.keys()):
        print("Invalid city data Entry")
        city = input('What city data you would like to explore? e.g. Chicago').title()

    #Get user input to fileter by month, day or both
    month_day = input('Would like to filter the data by month, day or both? ').lower()
    while month_day not in (['month', 'day', 'both', 'none']):
        print('Invalid data entry, just enter month, day or both! ')   
        month_day = input('Would like to filter the data by month, day or both? ').lower()

    #Now, get user input for specific month, specific day or both
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    if month_day == 'month' or month_day == 'both':
        month = input('Enter the specific month between january to june ').lower()
        while month not in months:
            print('which month -january, february, march, april, may, june! ').lower()
    else:
        month = 'all' 

    #After getting month data, now it is for entering which day user would like to see the data
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if month_day == 'day' or month_day == 'both':
        day = input('Enter the any day of the week! ').title()
        while day not in days:
           print('Invald entry for day!!!')
           day = input('Enter the any day of the week! ').title()


    else:
        day = 'all'

    print('-'*40)
    return city, month, day     