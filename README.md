# movie_map
This program contains several modules such as: data_from_list, get_coordinates, haversine_calc, movie_map, user_input, all_countries, main.
1. data_from_list: works with the given locations.list file and extracts data from it.
2. haversine_calc: module uses haversine library, contains functions to get distances between different coordinates.
3. movie_map: uses folium library, contains functions designed to work with .html map and perform several operations, such as creating map or adding markers/lines to the map
4. user_input: contains functions designed to get input from user and extract data from it.
5. all_countries: contains functions designed to get data from 28 .csv files, which contain country names in 28 different languages. Designed to get english country name by given native country name.
6. main: uses all of the above described modules to create an interactive .html map.

The map contains information with markers that represent movie filming location and lines that connect user location with markers

Enter your location. Use several comma-separated values for more accurate result: Хрещатик, Київ
Enter a year: 2018
![movie map](https://github.com/Michael-Data-Science-spec/movie_map/blob/main/image_2021-02-14_20-20-01.png?raw=true)

Enter your location. Use several comma-separated values for more accurate result: Los Angeles, CA
Enter a year: 2009
![movie map](https://github.com/Michael-Data-Science-spec/movie_map/blob/main/image_2021-02-15_11-13-55.png?raw=true)

html file consist of standart structure tags
* html
  * head
    * meta
    * /meta
    * link
    * /link
    * script
    * /script
  * /head
  * body
    * div
    * /div
    * script
    * /script
  * /body
* /html
