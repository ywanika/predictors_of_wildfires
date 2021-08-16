import netCDF4 as nc
import numpy as np
from matplotlib import pyplot as plt
import pickle

"""fn = "data/Out_gridMet/out_pet1980.nc"
ds = nc.Dataset(fn)

pet = np.array(ds['potential_evapotranspiration'])
#replace water with nan (not a number)
pet[pet == 3.2767e+04] = np.nan

pickle.dump( pet, open( "data/Out_gridMet/numpy/out_pet1980.pickle", "wb" ) )"""

#print (pet[:10,0:10,0:10])

#checking we have CA
#print(pet[0,:,:].shape)
#plt.imshow(pet[0, :, :]) #turns the data into image, showing first day
#plt.show()

#names = ["bi", "tmmn", "tmmx"]

#fn = "data/Out_gridMet/out_pet1980.nc"