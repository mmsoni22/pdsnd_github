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

def load_data(city, month, day):
    #Load the city data and filter it by month and day if applicable

    #Load the data into dataframe
    df = pd.read_csv(CITY_DATA[city])

    #Convert start time column into datetime column
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract the month and day from start time to create new column
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    #filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        #filter by month to create new dataframe
        df = df[df['month'] == month]

    #filter by day of the week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df        

def time_stats(df):
    #Display the statistics of most frequent time of travel

    print('\nCalculating the most frequent time of travel...\n')
    start_time = time.time()

    #Display the most frequent month of travel
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    print('/Most common month of travel is', months[popular_month-1])

    #Display the most common day of the week
    popular_day = df['day_of_week'].mode()[0]
    print('Most commmon day of the week for travel is', popular_day)

    #Display the most common hour of the day for travel
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most popular hour of the day for travel is', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    #Display the statistics on most popular stations and trip
    print('\nCalculating the most popular stations and trip...\n')
    start_time = time.time()
    
    #Most popular start station for picking up the bikes
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station for picking up the bike is', popular_start_station)

    #Most popular end statoin for dropping off the bikes
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end statoin for dropping off the bike is', popular_end_station)

    #Display the combination of most frequent start station and end station
    popular_trip = df['Start Station'] + 'to' + df['End Station']
    combination = popular_trip.mode()[0]
    print('Most popular trip is', combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    from datetime import timedelta as td
    #Display the statistics on total and average trip duration

    print('\nCalculating trip duration...\n')
    start_time = time.time()

    #Calculating Total time of travel
    total_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).sum()
    days =  total_travel_duration.days
    hours = total_travel_duration.seconds // (60*60)
    minutes = total_travel_duration.seconds % (60*60) // 60
    seconds = total_travel_duration.seconds % (60*60) % 60

    print('Total travel time is', days, 'days', hours, 'hours', minutes, 'minutes', seconds, 'seconds.')

    #Calculating the Average trip duration
    average_travel_duration = (pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])).mean()
    days =  average_travel_duration.days
    hours = average_travel_duration.seconds // (60*60)
    minutes = average_travel_duration.seconds % (60*60) // 60
    seconds = average_travel_duration.seconds % (60*60) % 60

    print('Average travel time is', days, 'days', hours, 'hours', minutes, 'minutes', seconds, 'seconds.')

def user_stats(df):
    #display the statistics on bikeshare users

    print('\nCalculating User stats...\n')
    start_time = time.time()

    user_type = df['User Type'].value_counts()
    print(user_type)

    #Display the type of gender
    if 'Gender' in (df.columns):
        gender = df['Gender'].value_counts()
        print(gender)

    #Display the earliest, most recent and most common date of birth
    if 'Birth Year' in (df.columns):
        year = df['Birth Year'].fillna(0).astype('int64')
        print('Earliest birth year is', year.min(), '\nMost recent birth year is', year.max(), '\nMost common birth year is', year.mode()[0])

        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)    

def display_raw_data(df):
    #display raw data and print 5 raw data at a time
    raw = input('\nWould you like to display the raw data!\n')
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count + 5])
            count =+ 5
            ask = input('Next 5 raws?')
            if ask.lower() != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break    

if __name__ == "__main__":
	main()
