import numpy as np
import pickle
import os
import datetime, calendar

titles = ["fm100", "pet", "pr", "sph", "srad", "th", "tmmn", "tmmx", "vs"]

#get feb 29th day
f_date = datetime.date(2000, 1, 1)
l_date = datetime.date(2000, 2, 29)
delta = l_date - f_date
leapDayNum = delta.days

for title in titles:

    fn = title + ".pickle"
    temp_array = pickle.load(open("data/pickle_gridMet/" +fn, "rb")) #[20][366, 238, 278

    for year in range (0, 21): #[2000,2021)
        if not calendar.isleap(year):
            #replace the year in the array with that year without feb 29th
            temp_array[year] = np.delete(temp_array[year], [leapDayNum], axis=0) 

    pickle.dump(temp_array, open( "data/pickle_gridMet2/"+fn, "wb" ) )

    