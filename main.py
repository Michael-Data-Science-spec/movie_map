"""
main module uses
    user_input
    get_coordinates
    all_countries
    data_from_list
    haversine_calc
    movie_map
    random
modules in order to create .html map
"""

import user_input
import get_coordinates
import all_countries
import data_from_list
import haversine_calc
import movie_map
import folium
import random

user_inp = user_input.get_user_location()
user_country = user_input.get_user_country(user_inp)
user_year = user_input.user_year()
user_coordinates = user_input.user_location_to_coordinates(user_inp)

country_names = all_countries.country_names()
english_names = all_countries.get_english_country_names(country_names)

for idx, name in enumerate(country_names):

    if user_country in name:
        user_country = english_names[idx]
        break


year_df = data_from_list.get_films_by_year(user_year)

if year_df.shape[0] > 275:
    country_df = data_from_list.get_films_by_country(user_country, df=year_df)

    if country_df.shape[0] < 125:
        country_df = year_df.sample(200)

else:
    country_df = year_df

country_year_df = country_df

print('calculating coordinates...')

coordinates = get_coordinates.get_latt_long(country_year_df)
movie_names = country_year_df['title'].tolist()

print('calculating distances...')

distances = haversine_calc.get_distances(user_coordinates, coordinates)
distances = [(dist, idx) for idx, dist in enumerate(distances)]
distances = sorted(distances)

print('getting ten places...')

ten_places = [(coordinates[idx], movie_names[idx]) for dist, idx in distances[:10]]


fg_marker = folium.FeatureGroup('Markers')
fg_line = folium.FeatureGroup('Lines')

world_map = movie_map.create_map(user_coordinates)
# fg_marker = movie_map.add_marker(world_map, user_coordinates, fg_marker=fg_marker, poppup='Ви тут', colour='darkred', get_icon='home')
fg_marker.add_child(folium.Marker(location=[user_coordinates[0], user_coordinates[1]],
                    popup='Ви тут',
                    icon=folium.Icon(color='darkred', icon='home'),
                    ))

print('generating map...')

for idx, place in enumerate(ten_places):

    # fg_marker = movie_map.add_marker(world_map, place[0], fg_marker=fg_marker, poppup='{}\nmovie location {}'.format(place[1], idx + 1))
    # fg_line = movie_map.draw_line(world_map, user_coordinates, place[0], fg_line=fg_line)
    fg_line.add_child(folium.PolyLine([user_coordinates, place[0]], color='yellow', weight=1))
    fg_marker.add_child(folium.Marker(location=[place[0][0], place[0][1]],
                        popup='{}\nmovie location {}'.format(place[1], idx + 1),
                        icon=folium.Icon(color='cadetblue', icon='film'),
                        ))

world_map.add_child(fg_marker)
world_map.add_child(fg_line)

world_map.save('movie_map.html')
