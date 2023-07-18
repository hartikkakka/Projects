import folium
import pandas

"""This Is project is made so that we can visualise the data on the map
 In this Data We have sample of Latitude, Longitude of certain police station to see 
 where the complaint rate is high and low  """

data = pandas.read_csv("police_station.txt")  # reading the CSV of police data
lat = list(data["Latitude"])  # converting latitude data in list
lon = list(data["Longitude"])  # converting longitude data in list
name = list(data["Police Station"])  # converting police station name in list
compl = list(data["Complaints Received (2020)"])  # converting complain data in list


"""This Function is created so we can see where the complain are more according to color """


def complaint_and_color(compl_no):
    if compl_no < 100:
        return "white"
    elif 101 < compl_no < 400:
        return "green"
    elif 401 < compl_no < 700:
        return "orange"
    else:
        return "red"


# Below is the first and most basic Function for creating a map on HTML
my_map = folium.Map(location=[19.20, 72.80], zoom_start=6, tiles="Stamen Terrain")
# Location is longitude and latitude
# zoom start means how much zoon should be there when map is opened
# tile "stamen Terrain" are provider of the Map

# Creating the variable so that it is easy change and filter out the option
fg = folium.FeatureGroup(name="My map")


for lt, ln, nam, comp in zip(lat, lon, name, compl):
    # zip function is like (1,2,3) and (4,5,6) output would be (1 and 4), (2and 5)so on
    fg.add_child(
        folium.CircleMarker(location=(lt, ln), radius=8, popup=nam, fill_color=complaint_and_color(comp), color="grey",
                            fill=True, fill_opacity=0.7))
# Location is longitude and latitude
# radius is how big the circle should be
# popup means when clicking the circle what data will be shown
# fill_color means the color from the function
# Color means the boarder color of the circle


my_map.add_child(fg)  # This is created so that we can create multiple profile type
my_map.add_child(folium.LayerControl())  # this is used the filter the profile type and other filtering
my_map.save("Mapl.html")  # saving all the data from above and naming the map file and running it
