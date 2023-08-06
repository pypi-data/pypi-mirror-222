import plotly.express as px
import pandas as pd
import sys
sys.path.append('/Users/apple/Desktop/s1282006_learn/s1282006_learn/statistics')
from frequenciesOfItems import frequenciesOfItems
class heatMapItemsFrequencies:
    def __init__(self, freq_dict):
        self.freq_dict = freq_dict
    def prepare_dataframe(self):
        lat = []
        lon = []
        freq = []

        for point, frequency in self.freq_dict.items():
            point = str(point)  # ensure point is a string
            point = point.replace("'", "")  # remove "'" characters
            point = point.replace("(", "")  # remove "(" characters
            point = point.replace(")", "")  # remove ")" characters
            point = point.replace("Point", "")  # remove "Point" string
            point = point.replace("[", "")  # remove "[" characters
            point = point.replace("]", "")
            coordinates = point.strip().split()  # trim spaces and split into components
            if len(coordinates) >= 2:  # check if coordinates contains at least 2 elements
                try:
                    lon.append(float(coordinates[0]))
                    # split latitude into actual value and extraneous part
                    latitude_parts = coordinates[1].split('.')
                    # use only the actual latitude value
                    lat.append(float(latitude_parts[0] + '.' + latitude_parts[1]))
                    freq.append(frequency)
                except ValueError:
                    print(f"Invalid coordinates: {coordinates}")
                    continue
            else:
                print(f"Incorrectly formatted point: {point}")

        return pd.DataFrame({
            'lon': lon,
            'lat': lat,
            'freq': freq
    })

    def plot_heatmap(self):
        df = self.prepare_dataframe()

        fig = px.density_mapbox(df, lat='lat', lon='lon', z='freq', radius=10,
                                center=dict(lat=36.686567, lon=135.52000), zoom=4,
                                mapbox_style="open-street-map")

        fig.show()

# usage
itemsFrequencies = frequenciesOfItems('PM24HeavyPollutionRecordingSensors.csv', ',')
itemsFreqDictionary = itemsFrequencies.getFrequencies()

heatMap = heatMapItemsFrequencies(itemsFreqDictionary)
heatMap.plot_heatmap()
