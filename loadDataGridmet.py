import netCDF4 as nc
import numpy

fn = "data/GridMet/pet_1980.nc" #speciific humidity
ds = nc.Dataset(fn)

#print(ds)  #print dataset
print(ds.__dict__) #metadata as dctionary
"""for dim in ds.dimensions.values(): 
    print(dim) #metadate for dimension classes"""
#ds.dimensions['x'] #access induvidual 
"""for var in ds.variables.keys(): 
    print(var) #variable metadata"""
#print(ds["potential_evapotranspiration"].sel(lon=-100, lat=30, day=5))
#print( len(ds['potential_evapotranspiration'])) #366 = arry for each day