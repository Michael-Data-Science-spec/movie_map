"""
module to work with geopy and coordinates
"""

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
import random

def get_latt_long(country_year):
    """
    gets longtitude and lattitude of every location in the list
    """
    location_lst = country_year['location'].tolist()
    location_lst = [','.join(loc.split(',')[-3:]) for loc in location_lst]
    geolocator = Nominatim(user_agent='my_app')
    coordinates_lst = []
    for loc in location_lst:

        try:
            coordinates_lst.append(geolocator.geocode(loc))
        except GeocoderUnavailable:
            coordinates_lst.append(None)

    coordinates_lst = [(coordinate.latitude + random.randint(-1000, 1000)/2000, coordinate.longitude
                       + random.randint(-1000, 1000)/2000)
                       for coordinate in coordinates_lst if coordinate != None]

    return coordinates_lst



