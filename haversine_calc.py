"""
module to calculate distances using haversine formula
"""

from haversine import haversine as hv

def calculate_distance(coor1: tuple, coor2: tuple):
    """
    calculates distance between two coordinates
    """
    dist = hv(coor1, coor2)

    return dist


def get_distances(initial_coor, coor_lst: list):
    """
    calculates dictance to specific coordinate coordinate
    for every coordinates in coor_lst
    returns list of distances
    """
    dist_lst = [calculate_distance(initial_coor, coor) for coor in coor_lst]

    return dist_lst
