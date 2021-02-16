"""
module is designed to work with 28 csv files that
contain country names in different languages
"""

"""
this module works with multiple csv files to extract
country names in different languages
"""

import pandas as pd


def read_country(alpha2: str):
    """
    reads country fil
    """
    df = pd.read_csv('{}.countries.csv'.format(alpha2), delimiter=',', usecols=['id', 'name'], index_col='id')
    df.columns = [alpha2]
    return df


def country_names():
    """
    creates list of country names in different languages
    """    
    alphas = ('ar', 'cs', 'da', 'de',
            'ee', 'el', 'en', 'es',
            'eu', 'fi', 'fr', 'hu',
            'lt', 'ja', 'ko', 'it',
            'nl', 'no', 'pl', 'pt',
            'ro', 'ru', 'sk', 'sv',
            'th', 'uk', 'zh', 'zh_tw')

    all_countries_df = [read_country(alpha) for alpha in alphas]
    all_countries = pd.merge(all_countries_df[0], all_countries_df[1], on=['id'])

    for idx in range(2, 28):
        all_countries = pd.merge(all_countries, all_countries_df[idx], how='inner', on=['id'])
    
    country_names_lst = [tuple(x) for x in all_countries.to_numpy()]
    return country_names_lst



def get_english_country_names(country_names_lst=country_names()):
    """
    gets english country names
    and returns it as a list
    """
    english_names = [x[6] for x in country_names_lst]
    return english_names
