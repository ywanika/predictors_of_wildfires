#Will load the data, crop it, convert it to a Numpy array, and save it in a pickle file

import netCDF4 as nc
import numpy as np
from matplotlib import pyplot as plt
import pickle
import os

titles = {"fm100":"dead_fuel_moisture_100hr", "pet":"potential_evapotranspiration", "pr":"precipitation_amount", "sph":"specific_humidity", "srad":"surface_downwelling_shortwave_flux_in_air", "th":"wind_from_direction", "tmmn":"air_temperature", "tmmx":"air_temperature", "vs":"wind_speed"}
#var_name = ["dead_fuel_moisture_100hr", "potential_evapotranspiration", "precipitation_amount", "specific_humidity", "wind_from_direction", "air_temperature", "air_temperature", "wind_speed"]

for title, var_name in titles.items():
    for year in range(2000, 2021, 1):
        
        name = title + "_" + str(year)

        #crop
        os.system(' ncea -d lat,32.3,42.2 -d lon,-124.7,-113.1 "data/' + name + '.nc" "data/out/' + name + '.nc"')
        print("cropped:", name)

        #load
        fn = "data/out/" + name + ".nc"
        ds = nc.Dataset(fn)

        #to numpy
        tempArray = np.array(ds[var_name])
        tempArray[tempArray == 3.2767e+04] = np.nan #replace water with nan (not a number)
        print("convert to numpy:", name)

        #pickle
        pickle.dump( tempArray, open( "data/out/"+title+".pickle", "wb" ) )
        print("put in pickle:", name)