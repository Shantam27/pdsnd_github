import pandas as pd
import numpy as np
import time
import datetime
CITY_DATA = { 'chicago': 'cities/chicago.csv',
              'new york city': 'cities/new_york_city.csv',
              'washington': 'cities/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("\Welcome to the program! Please choose your city:\n")
    print("1. Chicago 2. New York City 3. Washington\n")
    city=""
    day=""
    month=""
    while city not in CITY_DATA.keys():
        city = input().lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    """Creating dictionary for months"""
    Months = {'january':1, 'february':2 ,
                'march':3,'april':4, 'may':5, 'june':6, 'all':7 }
    print("\nPlease enter the month between January to June or type 'all' to see data from all months. Please enter full name (e.g. January)\n")

    while month not in Months.keys():
        month=input().lower()



    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    """Creating list of days in a week"""
    Days=['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    print("Please enter a day of the week (e.g Monday) or type 'all' if you don't want to filter on the basis of days")
    while day not in Days:
        day=input().lower()


    print('-'*70)
    return city, month, day

def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    """using value_count and idxmax to find the most occuring value"""
    popular_month = df['month'].value_counts().idxmax()
    print("\nMost popular month is: ",popular_month)

    # TO DO: display the most common day of week
    popular_day= df['day_of_week'].value_counts().idxmax()

    print("\nMost popular day of the week is:",popular_day )

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    #print(df.head())
    most_common_hour = df['hour'].value_counts().idxmax()
    print("Most popular hour is: ",most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    """using value_count and idxmax to find the most occuring value"""

    common_start_station=df['Start Station'].value_counts().idxmax()

    print("Most common start station is: ",common_start_station)
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()

    print("\nMost common end station is: ",common_end_station)
    #print(df)
    # TO DO: display most frequent combination of start station and end station trip
    """groupying start station and end station to find the most frequent combination"""
    combination= df.groupby(['Start Station','End Station' ]).size().idxmax()

    print("\nMost frequent combination of trips are from {} to {}".format(combination[0],combination[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    """using sum to calculate total trip duration"""
    trip_duration= df['Trip Duration'].sum()
    #total_time=str(datetime.timedelta(seconds=trip_duration))
    """using divmod as it gives both quotient and remainder"""
    minute, second = divmod(trip_duration, 60)
    hour, minute = divmod(minute,60)
    print("\ntotal trip duration is {} hour's {} minutes and {}seconds ".format(hour,minute,second))

    # TO DO: display mean travel time
    """using mean to calculate average duration"""
    average_trip_time=df['Trip Duration'].mean()

    minutes, seconds = divmod(average_trip_time, 60)
    if minutes > 60:
        hour, minute = divmod(minute,60)
        print("\ntotal trip duration is {} hour's {} minutes and {}seconds ".format(hours,minutes,seconds))
    else:
        print("\ntotal trip duration is {} minutes and {}seconds ".format(minutes,seconds))

    #print(df.head())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    """using value_counts as it group by all the value in columns"""
    user_types=df['User Type'].value_counts()
    print(user_types)


    # TO DO: Display counts of gender
    print('\nCalculating Gender Stats...\n')
    while True:
        try:
            gender_count=df['Gender'].value_counts()
            print(gender_count)
            break
        except:
            print("Sorry! Gender details are not present.")
            break

    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nCalculating birth details...\n')
    while True:

        try:
            most_common = df['Birth Year'].value_counts().idxmax()
            print("\nMost common year of birth is: ",int(most_common))

            """using idxmin to find the index and using index to find the particular element"""
            earliest=df['Birth Year'][df['Birth Year'].idxmin()]

            print("\nThe earliest year of birth: ",int(earliest))

            recent=df['Birth Year'][df['Birth Year'].idxmax()]

            print("\nThe recent year of birth: ",int(recent))
            break
        except:
            print("\nSorry! Birth details are not present.\n")
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)

def raw_data(df):
    start_time = time.time()
    data=""
    """creating a list for possible input outcomes"""

    Raw_data=['yes','no']
    print("\nDo you want to see raw data? Please type 'yes' or 'no' \n")
    while data.lower() not in Raw_data:
        data=input().lower()
        if data.lower() not in Raw_data:
            print("\nPlease enter valid input\n")
        elif data.lower() == 'yes':
            print(df.head())
        elif data.lower() == 'no':
            break

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*70)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
