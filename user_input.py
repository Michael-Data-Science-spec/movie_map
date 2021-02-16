"""
this module contains functions that work with the user input
"""

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable


def get_user_location():
    """
    gets user location
    """
    location = input('Enter your location.\n\
Use several comma-separated values for more accurate result: ')

    return location


def user_location_to_coordinates(user_location):
    """
    finds user lattitude and longtitude using user location
    """
    geolocator = Nominatim(user_agent='my_app')
    location = geolocator.geocode(user_location)
    latt_long = (location.latitude, location.longitude)

    return latt_long


def get_user_country(user_location):
    """
    gets user country using user input
    """
    geolocator = Nominatim(user_agent='my_app')
    location = geolocator.geocode(user_location)
    user_country = location.address.split(',')[-1].strip(' ')

    return user_country


def user_year():
    """
    gets user desired year
    """
    year = input('Enter a year: ')
    return year
