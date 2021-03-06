import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_data = ['january', 'february', 'march', 'april', 'may','june', 'all']
weekday_data = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Would you like to see data for Chicago, New York City, or Washington?')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = input('Enter the name of the city: ').lower()
    while city not in CITY_DATA.keys():
        print('Oops! Looks like you have entered a wrong city. Please try again! \n Choose between Chicago, New York City, or Washington')
        city = input('Enter the name of the city: ').lower()

    # get user input for month (all, january, february, ... , june)

    month = input('Enter the name of the month (type \'all\' for no filter): ').lower()
    while month not in month_data:
        print('Oops! Looks like you have entered a wrong month. Please try again!')
        month = input('Enter the name of the month (type \'all\' for no filter): ').lower()


    # get user input for day of week (all, monday, tuesday, ... sunday)

    day = input('Enter the name of the day of the week (type \'all\' for no filter): ').lower()
    while day not in weekday_data:
        print('Oops! Looks like you have entered a wrong weekday. Please try again!')
        day = input('Enter the name of the day of the week (type \'all\' for no filter): ').lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    #load the file into the data frame

    df = pd.read_csv(CITY_DATA[city])

    #convert Start Time and End Time to datatime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    #get month / week day / hour from Start Time
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday
    df['hour'] = df['Start Time'].dt.hour

    # to apply filters by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = month_data.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # use the index of the weekday list to get the corresponding int
        day = weekday_data.index(day)
        # filter by day of week to create the new dataframe
        df = df[df['weekday'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
