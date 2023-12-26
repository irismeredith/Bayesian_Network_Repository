# This file performs pre-processing on the Brisbane travel data to get it into a form that we can perform structure
# learning on

# Author: Iris Meredith

# Last modified: 25/05/2021

# Imports

import pandas as pd

# Read data from a CSV file

brisbane_trip_data = pd.read_csv('brisbane_travel_data_detailed.csv')

# Drop unnecessary fields from the data

drop_list = ['Run', 'Operator', 'Ticket Type (Level 1)', 'Ticket Type (Level 2)', 'Ticket Type (Level 3)',  'DCU Device',
             'Origin Device', 'Destination Device', 'Trip ID', 'Employee Id', 'Vehicle', 'Journey ID', 'Smartcard ID',
             'Ticket Status']

brisbane_trip_data_reduced = brisbane_trip_data.drop(columns=drop_list)

print(brisbane_trip_data_reduced.columns)

# Convert time and date fields to python's datetime formats

# Revert conversion to date for zone range column

# This should ideally be in a loop, or better, a vectorised function. It's like this mostly because I was mucking around trying
# to figure out how to transform the data, then never refactored.

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('Jan', '1')

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('Feb', '2')

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('Mar', '3')

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('Apr', '4')

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('May', '5')

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('Jun', '6')

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('Jul', '7')

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('Aug', '8')

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('Sep', '9')

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('Oct', '10')

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('Nov', '11')

brisbane_trip_data_reduced['Zone Range'] = brisbane_trip_data_reduced['Zone Range'].str.replace('Dec', '12')


brisbane_trip_data_reduced['Operations Date'] = pd.to_datetime(brisbane_trip_data_reduced['Operations Date'])

brisbane_trip_data_reduced['Scheduled Start'] = pd.to_datetime(brisbane_trip_data_reduced['Scheduled Start'])

brisbane_trip_data_reduced['Actual Start'] = pd.to_datetime(brisbane_trip_data_reduced['Actual Start'])

brisbane_trip_data_reduced['Actual End'] = pd.to_datetime(brisbane_trip_data_reduced['Actual End'])

brisbane_trip_data_reduced['Boarding Time'] = pd.to_datetime(brisbane_trip_data_reduced['Boarding Time'])

brisbane_trip_data_reduced['Alighting Time'] = pd.to_datetime(brisbane_trip_data_reduced['Alighting Time'])

# Group dates by month and day of the week

brisbane_trip_data_reduced['Month'] = pd.DatetimeIndex(brisbane_trip_data_reduced['Operations Date']).month

brisbane_trip_data_reduced['Weekday'] = pd.DatetimeIndex(brisbane_trip_data_reduced['Operations Date']).weekday

# Group times by day slice

# Define the grouping function to pass to apply


def bin_hours(date_time):
    return date_time.hour


def bin_minutes(date_time):
    if date_time.minute < 5:
        return 1
    elif date_time.minute < 10:
        return 2
    elif date_time.minute < 15:
        return 3
    elif date_time.minute < 20:
        return 4
    elif date_time.minute < 25:
        return 5
    elif date_time.minute < 30:
        return 6
    elif date_time.minute < 35:
        return 7
    elif date_time.minute < 40:
        return 8
    elif date_time.minute < 45:
        return 9
    elif date_time.minute < 50:
        return 10
    elif date_time.minute < 55:
        return 11
    else:
        return 12


brisbane_trip_data_reduced = brisbane_trip_data_reduced[brisbane_trip_data_reduced['Boarding Time'].notnull()]

print(brisbane_trip_data_reduced['Boarding Time'].notnull().unique())

brisbane_trip_data_reduced['Tag_on_hour'] = brisbane_trip_data_reduced['Boarding Time'].apply(bin_hours)

print(brisbane_trip_data_reduced['Tag_on_hour'].notnull().unique())

brisbane_trip_data_reduced['Tag_off_hour'] = brisbane_trip_data_reduced['Alighting Time'].apply(bin_hours)

brisbane_trip_data_reduced['Tag_on_minute'] = brisbane_trip_data_reduced['Boarding Time'].apply(bin_minutes)

brisbane_trip_data_reduced['Tag_off_minute'] = brisbane_trip_data_reduced['Alighting Time'].apply(bin_minutes)

# Trip duration value: create a reduced column

brisbane_trip_data_reduced['Duration'] = pd.TimedeltaIndex(brisbane_trip_data_reduced['Alighting Time']
                                                          - brisbane_trip_data_reduced['Boarding Time']).seconds

# Drop superfluous columns

print(brisbane_trip_data_reduced['Zone Range'].dtype)

print(brisbane_trip_data_reduced['Zone Range'].str.split('-', 1))

brisbane_trip_data_reduced[['Zone Start', 'Zone End']] = brisbane_trip_data_reduced['Zone Range'].str.split('-', 1, expand=True)

drop_list = ['Operations Date', 'Scheduled Start', 'Actual Start', 'Actual End', 'Ticket Number', 'Boarding Time',
             'Alighting Time', 'Passengers', 'Fare', 'Stop', 'Service', 'Zone Range', 'Duration',
             'Month', 'Weekday']

brisbane_trip_data_reduced = brisbane_trip_data_reduced.drop(columns=drop_list)

# Dump processed file to a CSV

print(brisbane_trip_data_reduced)

brisbane_trip_data_reduced.to_csv('training_data.csv', index_label='Trip_ID')
