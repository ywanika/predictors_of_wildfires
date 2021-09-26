#creating array of inputs and labels for one year used to train model
import numpy as np
import pickle

fire = pickle.load(open("data/pickle_fire2/fire_final.pickle", "rb")) #[20][365/6, 238, 278]
fm100 = pickle.load(open("data/pickle_gridMet2/fm100.pickle", "rb"))
pet = pickle.load(open("data/pickle_gridMet2/pet.pickle", "rb"))
pr = pickle.load(open("data/pickle_gridMet2/pr.pickle", "rb"))
sph = pickle.load(open("data/pickle_gridMet2/sph.pickle", "rb"))
srad = pickle.load(open("data/pickle_gridMet2/srad.pickle", "rb"))
th = pickle.load(open("data/pickle_gridMet2/th.pickle", "rb"))
tmmn = pickle.load(open("data/pickle_gridMet2/tmmn.pickle", "rb"))
tmmx = pickle.load(open("data/pickle_gridMet2/tmmx.pickle", "rb"))
vs = pickle.load(open("data/pickle_gridMet2/vs.pickle", "rb"))

fire_flatten = fire[1].flatten()
fm100_flatten = fm100[1].flatten()
pet_flatten = pet[1].flatten()
pr_flatten = pr[1].flatten()
sph_flatten = sph[1].flatten()
srad_flatten = srad[1].flatten()
th_flatten = th[1].flatten()
tmmn_flatten = tmmn[1].flatten()
tmmx_flatten = tmmx[1].flatten()
vs_flatten = vs[1].flatten()

#note: get array of input = [258860, 9], label = [249204,9]
#getting array of input = [258860, 9], label = [249204, 1]
data_train = []
labels_train = []
for i in range(len(fm100_flatten)):
    truth_value = np.isnan(fm100_flatten[i]) or np.isnan(pet_flatten[i]) or np.isnan(pr_flatten[i]) or np.isnan(sph_flatten[i]) or np.isnan(srad_flatten[i]) or np.isnan(th_flatten[i]) or np.isnan(tmmn_flatten[i]) or np.isnan(tmmx_flatten[i]) or np.isnan(vs_flatten[i]) 
    if not truth_value:
        features = [ fm100_flatten[i], pet_flatten[i], pr_flatten[i], sph_flatten[i], srad_flatten[i], th_flatten[i], tmmn_flatten[i], tmmx_flatten[i], vs_flatten[i] ]
        data_train.append(features)
        labels_train.append([ fire_flatten[i] ])

pickle.dump(data_train, open( "data/inputs_for_model/data_train.pickle", "wb" ) )
pickle.dump(labels_train, open( "data/inputs_for_model/labels_train.pickle", "wb" ) )
print("done")