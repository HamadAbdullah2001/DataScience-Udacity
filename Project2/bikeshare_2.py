import time
import pandas as pd
import numpy as np

<<<<<<< HEAD
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
=======
# Hello

CITY_DATA = { 'chicago': 'chicago.csv', 'new york city': 'new_york_city.csv', 'washington': 'washington.csv' }
# List of the first six months names of the year.
months = np.array(['january', 'february', 'march', 'april', 'may', 'june'])
# List of the days names of the week.
days = np.array(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

def check_invalid(element, lst):
    """
    Check the validity of the user input.
    Args:
        (str) element - the element that we will check if it is in the list or not.
        (list) lst - the list that we will search in for the element.
    Returns :
        True if the element ele in the list lst
    """

    return element in lst
>>>>>>> documentation

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
<<<<<<< HEAD

=======
>>>>>>> documentation
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
<<<<<<< HEAD
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs


    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)

=======

    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        print('Would you like to see data for Chicago, New York, or Washinton?')
        # get user input for city (chicago, new york city, washington).
        city = input('').lower()
        # check the validity of the input.
        if check_invalid(city, list(CITY_DATA.keys())):
            break
        print('OPS!! Invalid input, Try again!!')

    while True:
        print('Which month? January, February, March, April, May, and June?')
        # get user input for month (all, january, february, ... , june).
        month = input('').lower()
        # check the validity of the input.
        if check_invalid(month, months):
            break
        print('OPS!! Invalid input, Try again!!')

    while True:
        print('Which day? Please type your response as an integer (e.g., 1=Sunday).')
        # handling the unexpected input values
        try:
            # get user input for day of week (all, monday, tuesday, ... sunday).
            day = int(input(''))
            # check the validity of the input.
            if day >= 1 and day <= 7:
                day = days[day - 1]
                if check_invalid(day, days):
                    break
            else:
                print('OPS!! Invalid input, Try again!!')
        except ValueError:
            print('Invalid input, not a number')
>>>>>>> documentation

    print('-'*40)
    return city, month, day

<<<<<<< HEAD

=======
>>>>>>> documentation
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

<<<<<<< HEAD

    return df


=======
    # load the data for specific city.
    df = pd.read_csv(CITY_DATA[city.lower()])
    # delete unnecessary column from the data frame.
    df.drop(['Unnamed: 0'], inplace=True, axis=1)
    # clean the NaN values of the data frame.
    df.fillna(method='ffill', axis=0, inplace=True)

    # convert Start Time column to the datetime datatype using the pandas to_datetime() method.
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create new column called month, and assign the month value from Start Time column to it.
    df['month'] = df['Start Time'].dt.month
    # create new column called day_of_week, and assign the day_name() value from Start Time column to it.
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # create new column called hour, and assign the hour value from Start Time column to it.
    df['hour'] = df['Start Time'].dt.hour

    # check if the user select all months or not.
    if month != 'all':
        # if not, put the month values in the month column
        month = np.where(months == month.lower())[0][0] + 1
        df = df[df['month'] == month]

    # check if the user select all days or not.
    if day != 'all':
        # if not, put the day values in the day_of_week column
        df = df[df['day_of_week'] == day.lower().title()]

    return df

>>>>>>> documentation
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

<<<<<<< HEAD
    # display the most common month


    # display the most common day of week


    # display the most common start hour

=======
    # get the most common month from the data frame.
    most_common_month = df['month'].mode()[0]
    # display the most common month
    print('Most Popular Month : ', most_common_month)
    # get the most common day of week from the data frame.
    most_common_day = df['day_of_week'].mode()[0]
    # display the most common day of week
    print('Most Popular Day : ', most_common_day)
    # get the most common hour from the data frame.
    most_common_hour = df['hour'].mode()[0]
    # display the most common start hour
    print('Most Popular Hour : ', most_common_hour)
>>>>>>> documentation

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

<<<<<<< HEAD

=======
>>>>>>> documentation
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

<<<<<<< HEAD
    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip

=======
    # get the most commonly used start station from data frame.
    most_common_start_duration = df['Start Station'].mode()[0]
    # display most commonly used start station.
    print('Most Common Start Duration : ', most_common_start_duration)
    # get the most commonly used end station from data frame.
    most_common_end_duration = df['End Station'].mode()[0]
    # display most commonly used end station.
    print('Most Common End Duration : ', most_common_end_duration)
    # calculate the value of most frequent combination of start station and end station trip.
    # get the value grouped by start station and end station with sorting.
    mct_from_start_to_end = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    # display most frequent combination of start station and end station trip.
    print('Most Common Trip From Start To End : ')
    print(mct_from_start_to_end)
>>>>>>> documentation

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

<<<<<<< HEAD

=======
>>>>>>> documentation
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

<<<<<<< HEAD
    # display total travel time


    # display mean travel time

=======
    # get the total travel time from the data frame.
    total_travel_time = df['Trip Duration'].sum()
    # display total travel time
    print('Total Travel Time : ', total_travel_time)
    # get the average travel time from the data frame.
    average_travel_time = df['Trip Duration'].mean()
    # display average travel time
    print('Average Travel Time : ', average_travel_time)
>>>>>>> documentation

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

<<<<<<< HEAD

def user_stats(df):
=======
def user_stats(df, city):
>>>>>>> documentation
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

<<<<<<< HEAD
    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth

=======
    # get the counts for each user types from the data frame.
    user_type_counters = df['User Type'].value_counts()
    print('user_type :')
    # Display counts of user types
    print(user_type_counters)
    if city != 'washington':
        print('gender :')
        # get the counts for each gender from the data frame.
        gender_counters = df['Gender'].value_counts()
        # Display counts of gender
        print(gender_counters)
        # get the earliest recent of birth year from the data frame.
        earliest_recent = df['Birth Year'].min()
        # Display earliest recent.
        print(earliest_recent)
        # get the most recent of birth year from the data frame.
        most_recent = df['Birth Year'].max()
        # Display most recent.
        print(most_recent)
        print('birth_year :')
        # get the most common year of birth from the data frame.
        most_common_year_of_birth = df['Birth Year'].mode()[0]
        # Display most common year of birth.
        print(most_common_year_of_birth)
>>>>>>> documentation

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

<<<<<<< HEAD
=======
def display_data(df):
    start_loc = 0
    while True:
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n")
        if view_data.lower() != 'no':
            if view_data.lower() == 'yes':
                print(df.iloc[start_loc:start_loc+5])
                start_loc += 5
            else:
                print()
        else:
            break
>>>>>>> documentation

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
<<<<<<< HEAD
        user_stats(df)
=======
        user_stats(df, city)
        display_data(df)
>>>>>>> documentation

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

<<<<<<< HEAD

if __name__ == "__main__":
	main()
=======
if __name__ == "__bikeshare_2__":
	main()
>>>>>>> documentation
