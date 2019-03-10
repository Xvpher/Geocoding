import geopy
import numpy as np
import pandas
from matplotlib import pyplot as plt
from geopy.geocoders import Nominatim, GoogleV3, TomTom, mapbox
def main():
     df = pandas.read_csv('Votes_2014.csv', sep=",", header=0, index_col=None)
     # df = df.loc[1:100,:]
     def get_latitude(x):
         return x.latitude
     def get_longitude(x):
         return x.longitude
     geolocator = Nominatim()
     geolocate_column = df.apply(lambda x: geolocator.geocode(x['PC Name'], timeout=10, exactly_one=True), axis=1)
     geolocate_column = geolocate_column.replace(to_replace='None', value=np.nan).dropna()
     df['latitude'] = geolocate_column.apply(get_latitude)
     df['longitude'] = geolocate_column.apply(get_longitude)
     df.to_csv('geocoding_output.csv')
     df1 = df.loc[:,['PC Name','latitude','longitude']]
     nanval = np.isnan(df1['latitude'])
     df[nanval].to_csv('nanvalue.csv')

if __name__ == '__main__':
    main()
