import pandas as pd
from copy import deepcopy as dc
import numpy as np

def preprocessing(data_frame, date_format):
    '''
    Preprocessing the data to more convenient form, deleting redundencies
    and people that do not belong to the dataset. Such as the cleaning lady.

    :param  data_frame (pd.DataFrame): representing the data we collected
            date_format: (str) representing the datetime format
    :return (pd.Dataframe): with changed date formats and cleaned data points

    '''

    # Setting date_format to default
    if date_format == None:
        date_format = '%d %B %Y'

    # Copying the dataframe to
    data_frame = dc(data_frame)
    try:
        # Taking the cleaning lady out of the data set, since she is not a student
        data_frame = data_frame[data_frame['pseudonym'] != 'Putzfrau']

        # Converting the date format to a convenient datetime structure
        data_frame.insert(2, 'date', '')
        data_frame['date'] = pd.to_datetime(data_frame['day'].astype(str) + ' ' + data_frame['month'] + ' ' + data_frame['year'].astype(str), format=date_format)


    except:
        months = {"DEC": 12, "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAI": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9,
                  "OKT": 10, "NOV": 11, "DEZ": 12}
        data_frame = data_frame.replace({'month': months})
        data_frame['date'] = pd.to_datetime(data_frame[['year', 'month', 'day']])

    # Drop redundant columns
    data_frame = data_frame.drop(columns=['day', 'month', 'year'])

    return data_frame






