#get all the fire pickle files to be [20][365,238,278]
import numpy as np
import pickle
import os

#get list of pickle files
files = os.listdir("data/pickle_fire")

#make list to hold 20 years of fires
fire_final = []

#loop through list of all years

    #get number of days in that year

    #make a numpy array of 365/6 by 238 by 278 of all zeros called fire_year

    #loop through files in year

        #get corresponding day of file

        #load pickle file as temp_array

        #turn brightness to 0s and 1s

        #fire_year[day,:,:] = temp_array

    #append year to fire_final

#pickle fire final
