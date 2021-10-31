#mask arrays to be used for the CNN
import numpy as np
import pickle
from matplotlib import pyplot as plt

dir = 'test/lucien/' 
#contains an array for 2001, [365/6, 238, 278], features have nans for water
labels = pickle.load(open(dir + 'fire.pickle', "rb"))
fm100 = pickle.load(open(dir + 'fm100.pickle', "rb"))
pet = pickle.load(open(dir + 'pet.pickle', "rb"))
pr = pickle.load(open(dir + 'pr.pickle', "rb"))
sph = pickle.load(open(dir + 'sph.pickle', "rb"))
srad = pickle.load(open(dir + 'srad.pickle', "rb"))
th = pickle.load(open(dir + 'th.pickle', "rb"))
tmmn = pickle.load(open(dir + 'tmmn.pickle', "rb"))
tmmx = pickle.load(open(dir + 'tmmx.pickle', "rb"))
vs = pickle.load(open(dir + 'vs.pickle', "rb"))

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

mask_array = np.ma.getmask(np.ma.masked_invalid(features['fm100']))
for feature in features:
    mask_array += np.ma.getmask(np.ma.masked_invalid(features[feature]))

dir = "data/CNN_model_inputs/masked_arrays/"
labels = np.ma.masked_where(mask_array, labels)
pickle.dump(labels, open( dir+ "fire.pickle", "wb" ) )

for feature in features:
    pickle.dump(np.ma.masked_where(mask_array, features[feature]), open( dir+feature+".pickle", "wb" ) )