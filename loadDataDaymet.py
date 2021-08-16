import netCDF4 as nc
import numpy

fn = "data/Daymet/daymet_v3_prcp_1980_na.nc4"
ds = nc.Dataset(fn)

#print(ds)  #print dataset
#print(ds.__dict__) #metadata as dctionary
#for dim in ds.dimensions.values(): print(dim) #metadate for dimension classes
#ds.dimensions['x'] #access induvidual 
print("-" * 30)
for var in ds.variables.values(): 
    print(var) #variable metadata
#print(ds['prcp'][350, 4000:4005, 4000:4005]) #access specif variable data, returning 2d subset
#print( len(ds['prcp'])) #365, each day's precipitation
#print( ds['prcp'].shape)
#print (ds.keys())