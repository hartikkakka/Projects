# Police Station Complaints Map

This project creates an interactive map using Folium to visualize the complaint data of various police stations. The data includes the latitude, longitude, police station name, and number of complaints received in 2020. The map displays circles on the map representing each police station, with the color of the circle indicating the complaint rate.

## Installation

1. Make sure you have Python installed (version 3.7 or higher).
2. Install the required dependencies by running the following command:
   ```python
   pip install folium pandas

## Usage

1. Clone the repository or download the source code files.
2. Ensure you have a CSV file named "police_station.txt" with the required data columns (Latitude, Longitude, Police Station, Complaints Received (2020)).
3. Run the Python script.
4. The map will be generated and saved as "Mapl.html" in the current directory.
5. Open "Mapl.html" in a web browser to view the map.
6. The map displays circles representing each police station, with the size and color of the circle indicating the complaint rate.
7. Use the layer control in the top right corner to toggle the display of different layers (profiles).
8. Hover over a circle to see the name of the police station.
9. Customize the complaint thresholds and circle colors in the `complaint_and_color` function according to your needs.

## File Structure

- `main.py`: The main Python script that reads the data from "police_station.txt" and creates the interactive map using Folium.
- `police_station.txt`: The CSV file containing the police station data, including latitude, longitude, police station name, and complaints received.

## Dependencies

- `folium`: The Folium library used for creating interactive maps.
- `pandas`: The Pandas library used for reading and manipulating CSV data.

## Functions

- `complaint_and_color(compl_no)`: Assigns a color to the circle based on the number of complaints received. Customize the thresholds and colors in this function according to your needs.

## Output

The app generates an interactive map named "Mapl.html" that visualizes the police station data and complaint rates.
as `readme.md` in your project directory.