"""
module to work with .list file
and extract data from it
"""

import re
import pandas as pd

def read_data(file_name='locations.list'):
    """
    reads data from file
    """
    data = open(file_name, 'r')
    line = data.readline()
    while line != '==============\n':
        line = data.readline()

    data_lst = [line.replace('\'', '*') for line in data]
    return data_lst


def get_needed_data(data_name: str, data_lst=read_data()):
    """
    """
    data_prompts = {'titles': r'".*"',
                    'years': r'\(.{4}',
                    'locations': r'\t.*'}

    data_prompt = re.compile(data_prompts[data_name])
    data = [data_prompt.search(line).group() for line in data_lst]

    return data


def create_df(data_lst=read_data()):
    """
    creates pandas df from 3 lists
    """
    titles = [line.strip('\"') for line in get_needed_data('titles')]
    years = [line.strip('(') for line in get_needed_data('years')]
    locations = [line.strip('\t').split('\t')[0] for line in get_needed_data('locations')]
    df = pd.DataFrame({'title': titles,
                       'air_year': years,
                       'location': locations})
    return df


def get_films_by_country(country: str, df=create_df()):
    """
    returns df of films in specified country
    """
    df1 = df.loc[df.location.str.contains(country, regex=False)]
    if df1.empty:
        df1 = get_films_by_country('Ukraine', df)
    return df1


def get_films_by_year(year: str, df=create_df()):
    """
    returns df of films aired in specified year 
    """
    df1 = df.loc[df.air_year.str.contains(year, regex=False)]
    if df1.shape[0] < 10:
        return df
    return df1
