#creating dataframe of inputs and labels for one year used to train model
import numpy as np
import pickle
import pandas as pd

fire = pickle.load(open("data/pickle_fire2/fire_final.pickle", "rb")) #[20][365/6, 238, 278]
fm100 = pickle.load(open("data/pickle_gridMet_leap/fm100.pickle", "rb"))
pet = pickle.load(open("data/pickle_gridMet_leap/pet.pickle", "rb"))
pr = pickle.load(open("data/pickle_gridMet_leap/pr.pickle", "rb"))
sph = pickle.load(open("data/pickle_gridMet_leap/sph.pickle", "rb"))
srad = pickle.load(open("data/pickle_gridMet_leap/srad.pickle", "rb"))
th = pickle.load(open("data/pickle_gridMet_leap/th.pickle", "rb"))
tmmn = pickle.load(open("data/pickle_gridMet_leap/tmmn.pickle", "rb"))
tmmx = pickle.load(open("data/pickle_gridMet_leap/tmmx.pickle", "rb"))
vs = pickle.load(open("data/pickle_gridMet_leap/vs.pickle", "rb"))

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

df = pd.DataFrame(columns=["fire", "fm100", "pet", "pr", "sph", "srad", "th", "tmmn", "tmmx", "vs"])

for i in range(len(fm100_flatten)):
    truth_value = np.isnan(fm100_flatten[i]) or np.isnan(pet_flatten[i]) or np.isnan(pr_flatten[i]) or np.isnan(sph_flatten[i]) or np.isnan(srad_flatten[i]) or np.isnan(th_flatten[i]) or np.isnan(tmmn_flatten[i]) or np.isnan(tmmx_flatten[i]) or np.isnan(vs_flatten[i]) 
    if not truth_value:
        features = [ fire_flatten[i], fm100_flatten[i], pet_flatten[i], pr_flatten[i], sph_flatten[i], srad_flatten[i], th_flatten[i], tmmn_flatten[i], tmmx_flatten[i], vs_flatten[i] ]
        df_temp = pd.DataFrame([features], columns=["fire", "fm100", "pet", "pr", "sph", "srad", "th", "tmmn", "tmmx", "vs"])
        df = df.append(df_temp)
        
pickle.dump(df, open( "data/inputs_for_model/allData_df.pickle", "wb" ) )
print("done")