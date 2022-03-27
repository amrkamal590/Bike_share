# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 15:38:26 2021

@author: Amr
"""
#First import libraries i will need in the project.
import time
import numpy as np
import pandas as pd

#Adding the cities we will work on it
CITY_DATA = { "chicago" : "chicago.csv" , 
              "new york city" : "new_york_city.csv" ,
              "washington" : "washington.csv" }


def get_filters():
    
    '''
    Ask the user to enter city name , month name , day name to filter the data
    to analyze.
    it shuold returns :
    -City name (str)
    -whether specific month or all(str)
    -whether specific day or all  (str)
    ''' 
    
    print("Hi sir let\'s explore some us bikeshare")
    #we will use while loop to correct invalid inputs.
    city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()

    while city not in (CITY_DATA.keys()):
            print("Invalid input pls enter a city again")
            city = input('Would you like to see data for Chicago, New York City, or Washington? ').lower()

    #Filter the data by month, day or both"
    filter = input("Would you like to filter the data by month, day, both, or none?").lower()
    while filter not in(['month', 'day', 'both', 'none']):
        print("You entered a wrong filter pls try again")
        filter = input("Would you like to filter the data by month, day, both, or none?").lower()
    
    #if the user want to filter by month he should input the specific month.
    Months = ["january", "february", "march", "april", "may", "june"]
    if filter == "month" or filter == "both":
        month = input("Which month to filter:  january, february , march , april , may , june ").lower()
        while month not in Months:
            print("Invalid input pls enter month again")
            month = input("Which month to filter:  jan, feb , march , apr , may , jun ").lower()    
    else:
        month = "all"
    
    #if the user want to filter by month he should input the specific month.
    Days = ["saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
    if filter == "day" or filter == "both":
        day = input("Which day to filter:  saturday, sunday , monday , tuesday , wednesday , thursday , friday ").lower()
        while day not in Days:
            print("Invalid input pls enter day again")
            day = input("Which day to filter:  sat, sun , mond , tue , wen , thu , fri ").lower()    
    else:
        day = "all"
      
        
    print(" "*15 + "."*30)
    return city , month , day


def load_data(city , month , day):
     
    '''
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    '''
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the start time column to datetime
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
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
 
    '''A- Popular times of travel
             #1- most common month
             #2- most common day of week
             #3- most common hour of day
    '''         
    print("\nCalculating the most frequent Times of travel: ")
    Start_Time = time.time()
    
    #now by using mode method to find the most popular month
    popular_month = df["month"].mode()[0]
    print(f"\nMost popular month(1 = january,...,6=june): {popular_month}")    
    
    #now by using mode method to find the most popular day
    popular_day = df["day_of_week"].mode()[0]
    print(f"\nMost popular day: {popular_day}")
    
    #now by using mode method to find the most popular hour
    popular_hour = df["hour"].mode()[0]
    print(f"\nMost popular start hour: {popular_hour}")
    
    print(f"\nThis took { (time.time()-Start_Time ) } seconds.")
    #Time taken to perform the calculation
    
    
    print(" "*15 + "."*30)
 

def station_stats(df):
    ''' B- calculating:
               1-most common start station
               2- most common end station
               3- most common trip from start to end
    '''
    print("\ncalculating The most popular station and trip: ")
    Start_Time = time.time()
    #now by using mode method to find the most popular start station
    common_Start_Station = df["Start Station"].mode()[0]
    print("The most common Start Station: ", {common_Start_Station})
    
    #now by using mode method to find the most popular end station
    common_End_Station = df["End Station"].mode()[0]
    print("\nThe most common End Station: ", {common_End_Station})
    
    #now we calculate most common trip from start to end
    #then we calculate the most common trip by using mode method
    popular_trip = df["Start Station"] + ' to ' + df["End Station"]
    print('The most popular trip is: from: ',{popular_trip.mode()[0]})
    
    print(f"\nThis took { (time.time()-Start_Time ) } seconds.")
    #Time taken to perform the calculation
    
    print(" "*15 + "."*30)
    
    
def trip_duration_stats(df):
    ''' C- Trip duration
               1-total travel time
               2-average travel time
    '''
    print("\ncalculating Trip Duration: \n ")
    Start_Time = time.time()
    
    #now by using sum method to calculate total trip duration
    Total_Trip_Duration = df['Trip Duration'].sum()
    
    #The duration in minutes & seconds format
    minute, second = divmod(Total_Trip_Duration, 60) 
    
    #The duration in hour & minutes format
    hour, minute = divmod(minute, 60)
    print(f"\nThe total trip duration is {hour} hours,{minute} minutes and {second} seconds. ")
    
    #now we calculate average trip duration by using mean method
    average_duration =df["Trip Duration"].mean()
    print("\nThe average trip duration is : ", {average_duration})
    
    print(f"\nThis took { (time.time()-Start_Time ) } seconds.")
    #Time taken to perform the calculation
    
    print(" "*15 + "."*30)
    
    
def user_stats(df):
    ''' D- User info
            1-counts of each user type
            2-counts of each gender (only available for NYC and Chicago)
            3-earliest, most recent, most common year of birth
    '''
    print("\ncalculating User type stats:- \n ")
    Start_Time = time.time()
     
    #now by using value_counts method to calculate total users
    print(df['User Type'].value_counts())
        
    #now calculating counts of each gender except washington
    if 'Gender' in(df.columns):
        print(df['Gender'].value_counts())
        print('\n\n')
        
        #now calculating most earliest year of birth by min() method
        #now calculating most recent year of birth by max() method     
        #calculating earliest, most recent, most common year of birth by mode method
        if 'Birth Year' in(df.columns):
            year = df['Birth Year'].fillna(0).astype('int64')
            print(f'Earliest birth year is: {year.min()}\nmost recent is: {year.max()}\nand most comon birth year is: {year.mode()[0]}')
            
    print(f"\nThis took { (time.time()-Start_Time ) } seconds.")
    #Time taken to perform the calculation 
    
    print(" "*15 + "."*30)
    
    
def display_raw_data(df):
    """Ask the user if he wants to display the raw data and print 5 rows at time"""
    raw = input('\nWould you like to diplay raw data?\n')
    pd.set_option('display.max_columns',200)
    if raw.lower() == 'yes':
        count = 0
        while True:
            print(df.iloc[count: count+5])
            count += 5
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
      
      restart = input("\n Would you like to restart the program ?? Enter yes or no.\n")
      if restart.lower() != "yes":
          break
      
if __name__ == "__main__" :
        main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    