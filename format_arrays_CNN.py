import numpy as np
import pickle
from matplotlib import pyplot as plt
import random

dir = 'data/CNN_model_inputs/masked_arrays/' 
#contains an array for 2001 (365 days), [364/5 (cuz start at 0), 238, 278], features have nans for water
fire = pickle.load(open(dir + 'fire.pickle', "rb"))
fm100 = pickle.load(open(dir + 'fm100.pickle', "rb"))
pet = pickle.load(open(dir + 'pet.pickle', "rb"))
pr = pickle.load(open(dir + 'pr.pickle', "rb"))
sph = pickle.load(open(dir + 'sph.pickle', "rb"))
srad = pickle.load(open(dir + 'srad.pickle', "rb"))
th = pickle.load(open(dir + 'th.pickle', "rb"))
tmmn = pickle.load(open(dir + 'tmmn.pickle', "rb"))
tmmx = pickle.load(open(dir + 'tmmx.pickle', "rb"))
vs = pickle.load(open(dir + 'vs.pickle', "rb"))


###get fire and non-fire labels and coordinates
labels = []
coor = []
#get fire coordinates
for day in range(fire.shape[0]):
    row,col = np.ma.nonzero(fire[day, :, :])
    if row.size != 0:
        for point in range(row.size):
            coor.append((day, row[point], col[point]))
            labels.append(1)

#get non-fire coordinates 
n = len(coor) #2347
x=0
while x < n:
    day = random.randint(0, fire.shape[0]-1)
    row = random.randint(0, fire.shape[1]-1)
    col = random.randint(0, fire.shape[2]-1)
    if fire[day,row,col] == 0.0:
        coor.append((day, row, col))
        labels.append(0)
        x+=1

dir = "data/CNN_model_inputs/input_arrays/"

pickle.dump(coor, open( dir+ "coor.pickle", "wb" ) )

"""dir = "data/CNN_model_inputs/input_arrays/"
labels = pickle.load(open( dir+ "labels.pickle", "rb" ) )
coor = pickle.load(open( dir+ "coor.pickle", "rb" ) )"""

data = []
bad_indices = []
window_dim = 25
half_window = int(window_dim/2)
array_hieght = fm100.shape[1]
array_width = fm100.shape[2]

for i, c in enumerate(coor):
    if c[1] - half_window < 0 or c[1] + half_window > array_hieght or c[2] - half_window < 0 or c[2] + half_window > array_width:
        bad_indices.append(i)
    else:
        img_patch_fm100 = fm100[c[0], c[1] - half_window : c[1] + half_window, c[2] - half_window : c[2] + half_window]
        img_patch_pet = pet[c[0], c[1] - half_window : c[1] + half_window, c[2] - half_window : c[2] + half_window]
        img_patch_pr = pr[c[0], c[1] - half_window : c[1] + half_window, c[2] - half_window : c[2] + half_window]
        img_patch_sph = sph[c[0], c[1] - half_window : c[1] + half_window, c[2] - half_window : c[2] + half_window]
        img_patch_srad = srad[c[0], c[1] - half_window : c[1] + half_window, c[2] - half_window : c[2] + half_window]
        img_patch_th = th[c[0], c[1] - half_window : c[1] + half_window, c[2] - half_window : c[2] + half_window]
        img_patch_tmmn = tmmn[c[0], c[1] - half_window : c[1] + half_window, c[2] - half_window : c[2] + half_window]
        img_patch_tmmx = tmmx[c[0], c[1] - half_window : c[1] + half_window, c[2] - half_window : c[2] + half_window]
        img_patch_vs = vs[c[0], c[1] - half_window : c[1] + half_window, c[2] - half_window : c[2] + half_window]
        features_array = np.stack((img_patch_fm100, img_patch_pet, img_patch_pr, img_patch_sph, img_patch_srad, img_patch_th, img_patch_tmmn, img_patch_tmmx, img_patch_vs), axis = 2)
        data.append(features_array)

labels = [i for j, i in enumerate(labels) if j not in bad_indices]

pickle.dump(labels, open( dir+ "labels.pickle", "wb" ) )

#combine features into one array
"""features_array = np.empty((fm100.shape[0], fm100.shape[1], fm100.shape[2],9), dtype=float)

for day in range(fm100.shape[0]):
    for row in range(fm100.shape[1]):
        for col in range(fm100.shape[2]):
            fm100_val = fm100[day,row,col]
            pet_val = pet[day,row,col]
            pr_val = pr[day,row,col]
            sph_val = sph[day,row,col]
            srad_val = srad[day,row,col]
            th_val = th[day,row,col]
            tmmn_val = tmmn[day,row,col]
            tmmx_val = tmmx[day,row,col]
            vs_val = vs[day,row,col]
            features_array[day,row,col] = (fm100_val, pet_val, pr_val, sph_val, srad_val, th_val, tmmn_val, tmmx_val, vs_val)

pickle.dump(labels, open( dir+ "features_array.pickle", "wb" ) )"""
