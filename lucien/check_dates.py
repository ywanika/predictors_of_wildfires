'''
Check how fire incidence is distributed through each year; i.e., are fires concentrated during certain times of each year
'''

# 3rd party imports
import numpy as np
import pickle
from matplotlib import pyplot as plt

# Load data
dir = '/Users/lucien/Dropbox/Tutoring/Polygence/Anika 2021/predictors_of_wildfires/data/'
labels = pickle.load(open(dir + 'fire.pickle', "rb")) #[20][365/6, 238, 278]
fm100 = pickle.load(open(dir + 'fm100.pickle', "rb"))
pet = pickle.load(open(dir + 'pet.pickle', "rb"))
pr = pickle.load(open(dir + 'pr.pickle', "rb"))
sph = pickle.load(open(dir + 'sph.pickle', "rb"))
srad = pickle.load(open(dir + 'srad.pickle', "rb"))
th = pickle.load(open(dir + 'th.pickle', "rb"))
tmmn = pickle.load(open(dir + 'tmmn.pickle', "rb"))
tmmx = pickle.load(open(dir + 'tmmx.pickle', "rb"))
vs = pickle.load(open(dir + 'vs.pickle', "rb"))

# Save all features in dictoinary
features = {'fm100': fm100,
            'pet': pet,
            'pr': pr,
            'sph': sph,
            'srad': srad,
            'th': th,
            'tmmn': tmmn,
            'tmmx': tmmx,
            'vs': vs,
            }

# Count non-zeros per day
#mask_array = np.zeros_like(features['fm100'])
# for i in range(mask_array.shape[0]):
#     for j in range(mask_array.shape[1]):
#         for k in range(mask_array.shape[2]):
#             is_nan = False
#             for key in features.keys():
#                 if np.isnan(features[key][i,j,k]):
#                     is_nan = True
#                     break
#             mask_array[i,j,k] = np.nan
mask_array = np.ma.getmask(np.ma.masked_invalid(features['fm100']))

# Apply mask to labels
labels = np.ma.masked_where(mask_array, labels)

# expand positive fire label pixels
for d in range(labels.shape[0]):

    # find pixels that correspond to fires
    x,y = np.ma.nonzero(labels[d, :, :])  # 238 x 278 array
    for i, j in zip(x,y):
        labels[d, i-5:i+5, j-5:j+5] = 1.0


# count fires by day
num_fires_per_day = []
for d in range(labels.shape[0]):
    num_fires = np.ma.sum(labels[d, :, :])
    num_fires_per_day.append(num_fires)
# plot
if True:
    plt.plot(num_fires_per_day)
    plt.show()