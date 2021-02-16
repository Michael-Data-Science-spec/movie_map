"""
this module cantains functions which are used to
work with the folium library and .html map
"""

import folium

def create_map(user_location):
    """
    creates map centered at user location
    """
    world_map = folium.Map(location=[user_location[0], user_location[1]], zoom_start=6)
    return world_map
    # world_map.save('basic_map.html')


def add_marker(world_map, marker_loc, fg_marker, poppup='', colour='cadetblue', get_icon='film'):
    """
    adds marker at map using custom location
    """
    fg_marker.add_child(folium.Marker(location=[marker_loc[0], marker_loc[1]],
                  popup=poppup,
                  icon=folium.Icon(color=colour, icon=get_icon),
                 ))
    return fg_marker


def draw_line(world_map, loc1, loc2, fg_line):
    """
    adds a line to the map connecting markers
    """
    fg_line.add_child(folium.PolyLine([loc1, loc2], color='black', weight=1))
    return fg_line


def save_map(world_map, filename='movie_map.html'):
    """
    saves map as an html file
    """
    world_map.save(filename)
    return True
