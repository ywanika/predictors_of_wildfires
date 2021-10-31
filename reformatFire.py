#get all the fire pickle files to be [20][365,238,278] and turn brightness to 0s and 1s
import numpy as np
import pickle
import os
import datetime, calendar

#get list of pickle files
files = os.listdir("data/pickle_fire")

#make list to hold 20 years of fires
fire_final = []

#loop through list of all years
for year in range (2000, 2021):
    #get number of days in that year
    totDays = 365
    if calendar.isleap(year):
        totDays= 366
    #make a numpy array of 365/6 by 238 by 278 of all zeros called fire_year
    fire_year = np.zeros((totDays, 238,278))
    #loop through files in year
    files = []
    for file in os.listdir("data/pickle_fire/"):
        if file.startswith(str(year)):
            files.append(file)
            files.sort()
    for dayFN in files:
        #get corresponding day of file
        f_date = datetime.date(year, 1, 1)
        mo = dayFN[5:7]
        dy = dayFN[8:10]
        l_date = datetime.date(year, int(mo), int(dy))
        delta = l_date - f_date
        dayNum = delta.days
        #load pickle file as temp_array
        temp_array = pickle.load(open("data/pickle_fire/" +dayFN, "rb"))
        #turn brightness to 0s and 1s
        temp_array[temp_array >= 0] = 1
        temp_array[temp_array != 1] = 0
        #fire_year[day,:,:] = temp_array
        fire_year[dayNum,:,:] = temp_array
    #append year to fire_final
    fire_final.append(fire_year)
#pickle fire final
pickle.dump(fire_final, open( "data/pickle_fire2/fire_final.pickle", "wb" ) )
