import time
import pandas as pd
import numpy as np
from datetime import timedelta as td

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while True:
        cities = ["chicago", "new york city", "washington"]
        city = input("\nEnter city for which you want to explore: Chicago, New York City, Washington.: \n").lower()
        
        if city not in cities:
            print("\nPlease enter valid city name. \n")
            continue
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months = ["all", "january", "february", "march", "april", "may", "june"]
        month = input("\nEnter month(from January to June) for which you want to explore or else type 'all' for no month filter.: \n").lower()
        
        if month not in months:
            print("\nPlease enter valid month. \n")
            continue
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days = ["all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        day = input("\nEnter day of week which you want to explore or else type 'all' for no day filter.: \n").lower()
        
        if day not in days:
            print("\nPlease enter valid day. \n")
            continue
        break            

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
    df = pd.read_csv(CITY_DATA[city])
#     df = df.dropna()
        
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Month"] = df["Start Time"].dt.month
    df["Day"] = df["Start Time"].dt.weekday_name
    
    if month != 'all':
        
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    
    if day != 'all':
        df = df[df['Day'] == day.title()]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ["january", "february", "march", "april", "may", "june"]
    popular_month = months[df["Month"].mode()[0] - 1].title()
    print("Most common month is: ", popular_month)

    # TO DO: display the most common day of week
    popular_day = df["Day"].mode()[0]
    print("Most common day of week is: ", popular_day)

    # TO DO: display the most common start hour
    df["Start Hour"] = df["Start Time"].dt.hour
    
    popular_start_hour = df["Start Hour"].mode()[0]
    print("Most common start hour is: ", popular_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df["Start Station"].mode()[0]
    print("Most commonly used start station is: ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df["End Station"].mode()[0]
    print("Most commonly used end station is: ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station_combination = df.groupby(["Start Station", "End Station"]).size().sort_values(ascending=False)
    print("Most frequent combination of start station and end station trip is: ", popular_start_end_station_combination.index[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time_seconds = df["Trip Duration"].sum()
    total_travel_time = td(seconds = int(total_travel_time_seconds))
    print("Total travel time is: ", total_travel_time)
    
    # TO DO: display mean travel time
    mean_travel_time_seconds = df["Trip Duration"].mean()
    mean_travel_time = td(seconds = int(mean_travel_time_seconds))
    print("Mean travel time is: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df["User Type"].value_counts()
    print("Breakdown of user types:\n",user_type)

    # TO DO: Display counts of gender
    if "Gender" in df.columns.values:
        gender = df["Gender"].value_counts()
        print("\nBreakdown of gender: \n",gender)
    else:
        print("\nNo Gender data to share. \nNone")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns.values:
        oldest = df["Birth Year"].sort_values().values[0]
        youngest = df["Birth Year"].sort_values(ascending = False).values[0]
        common_year_birth = df["Birth Year"].mode()
        
        print("\nOldest, Youngest and most popular year of birth, respectively is: \n", oldest, ", ", youngest, ", ", common_year_birth)
    else:
        print("\nNo Birth Year data to share. \nNone")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    
    c = 0
    print("\nFirst 5 raw data\n")
    while True:
        print(df.iloc[c:(c+5), :])
        c += 5
        print("-"*40)
        s = input("\nDo you want to see next five raw data? Type 'yes' to continue or anything else to terminate.\n")
        if s.lower() != "yes":
            break
        print("\nNext 5 raw data\n")

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
