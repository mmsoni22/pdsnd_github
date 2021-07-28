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
