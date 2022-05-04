import time
import pandas as pd
import numpy as np
import calendar

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
        city = input('Please Choose the city you want from Chicago, New York or Washington? \n> ').lower()
        if city not in CITY_DATA.keys():
           print('please enter the city you want')
        else: break
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('please enter a month from january to june or type "all" to display all months: ').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month != 'all' and month not in months:
            print('please enter a valid month name')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('please enter one of the weak days or type "all" to display all days: ').lower()
        days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday','thursday', 'friday']
        if day != 'all' and day not in days:
            print('please enter a valid day name')
        else:
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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('Most Common Month is: {}'. format(df['month'].mode()[0]))
    
    
    # TO DO: display the most common day of week
    print('Most Common Day is: {}'. format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print('Most Common start hour is: {}'. format(df['hour'].mode()[0]))
    


    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most Common start station is: {}'. format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('Most Common End atation is: {}'. format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station']+ "," + df['End Station']
    print('Most Common route is: {}'. format(df['route'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum().round()
    print("Total travel time :", total_travel)

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean().round()
    print("Mean travel time :", mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts().to_frame())

    # TO DO: Display counts of gender
    if city != 'washington':
          print(df['Gender'].value_counts().to_frame())
                   

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Most common birth year is : ',int(df['Birth Year'].mode()[0]))
        print('the most Recent birth year : ',int(df['Birth Year'].max()))
        print('Earliest birth year : ',int(df['Birth Year'].min()))
    else:
        print('there is no available datat for this city')


     
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    #Tell the user if he want to show him 5 rows followed by other 5 rows until the end of the data.
    print('\nRaw date is available to check... \n')
    
    index=0
    user_input = input('Would you like to display 5 rows of the raw data? please type yes or No ').lower()
    if user_input not in ['yes', 'No']:
        print('That\'s invalid choice, please typr yes or No')
        user_input = input('Would you like to display 5 rows of the raw data? please type yes or No ').lower()
    elif user_input != 'yes':
        print('Thank you')
               
    else:
        while index+5 < df.shape[0]:
            print(df.iloc[index:index+5])
            index+=5
            user_input = input('Would you like to display more 5 rows of the raw data? ').lower()
            if user_input != 'yes':
                print('Thank you')
                break
        
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank you')
            break


if __name__ == "__main__":
	main()