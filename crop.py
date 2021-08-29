#ncea -d lat,32.3,42.2 -d lon,-124.7,-113.1 "data/GridMet/pet_1980.nc" "data/GridMet/out_pet1980.nc"
#ncea -d lat,32.3,42.2 -d lon,-124.7,-113.1 "data/Daymet/daymet_v3_prcp_1980_na.nc4" "data/Out_Daymet/out_prcp_1980.nc4"

#----------------------------

"""from nco import Nco
from nco import custom as c
nco = Nco()

opt = [
    c.Limit(dmn_name="lon", srt=32.3, end=42.2),
    c.Limit(dmn_name="lon", srt=-124.7, end=-113.1)
]

nco.ncks(input="data/fm100_2000_copy.nc", output= "data/out/fm100_2000_copy.nc", options=opt)"""

#---------------------------

"""import netCDF4 as nc
import numpy

fn = "data/Out_gridMet/out_tmmx1980.nc"
ds = nc.Dataset(fn)

for var in ds.variables.values(): 
    print(var) #variable metadata

#print( ds['prcp'].shape)"""

#---------------------------
"""import os
os.system(' ncea -d lat,32.3,42.2 -d lon,-124.7,-113.1 "data/fm100_2000_copy.nc" "data/out/fm100_2000_copy.nc" ')"""