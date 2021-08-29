import netCDF4 as nc
import numpy as np
from matplotlib import pyplot as plt
import pickle
import pandas as pd
import random

#create variables to get array point from lat/lon coordinate
fn = "data/nc/fm100_2000.nc"
ds = nc.Dataset(fn)
lats = ds.variables['lat'][:] 
lons = ds.variables['lon'][:]

# Csv to dataframe
df = pd.read_csv ('data/DL_FIRE_M-C61_215362/fire_archive_M-C61_215362.csv')
#print(df.head())

# Make a list of all the unique dates
dates = df.acq_date.unique()
df_dates = df.groupby(by="acq_date")

# Loop through list
for date in dates:

    # Create new np array with NAN for date
    tempArray = np.empty((238,278))
    tempArray[:] = np.NaN

    # Loop through rows in unique date
    df_groupTemp = df_dates.get_group(date)
    fires_date = df_groupTemp.index.tolist()
    for index in fires_date:

        # Get array point for coordinate
        coordinate = (df.iloc[index]["latitude"], df.iloc[index]["longitude"])
        row = np.argmin( np.abs( lats - coordinate[0] ) )
        col = np.argmin( np.abs( lons - coordinate[1] ) )
        #print (row, col)

        # Set array point to brightness
        tempArray[row,col] = df.iloc[index]["brightness"]
        #print(tempArray[row,col])

        #check every once in a while
        if random.randint(0,10000) == 1:
            print (row, col)
            plt.imshow(tempArray)
            plt.show()

    # Dump to pickle
    pickle.dump(tempArray, open( "data/pickle/pickle_fire/"+str(date)+".pickle", "wb" ) )
    print("put in pickle:", str(date))