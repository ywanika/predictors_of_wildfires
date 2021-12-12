import numpy as np
import pickle
import matplotlib.pyplot as plt
import random

print ("loading files...")
data= pickle.load(open("data/inputs_for_model/data_train.pickle", "rb"))
labels = pickle.load(open("data/inputs_for_model/labels_train.pickle", "rb"))

#create lists of fire and non-fire values of equal size
print ("sorting fm100 data...")
fm100_data = [x[0] for x in data]
fm100_1s = [x for x,l in zip(fm100_data, labels) if l == 1.0]
fm100_0s = [x for x,l in zip(fm100_data, labels) if l == 0.0] # list of fm100 vals of no fire
fm100_0s = random.sample(fm100_0s, len(fm100_1s)) # get same number of fire and non-fire

print ("sorting pet data...")
pet_data = [x[1] for x in data]
pet_1s = [x for x,l in zip(pet_data, labels) if l == 1.0]
pet_0s = [x for x,l in zip(pet_data, labels) if l == 0.0]
pet_0s = random.sample(pet_0s, len(pet_1s))

print ("sorting pr data...")
pr_data = [x[1] for x in data]
pr_1s = [x for x,l in zip(pr_data, labels) if l == 1.0]
pr_0s = [x for x,l in zip(pr_data, labels) if l == 0.0]
pr_0s = random.sample(pr_0s, len(pr_1s))

print ("sorting pr data...")
pr_data = [x[1] for x in data]
pr_1s = [x for x,l in zip(pr_data, labels) if l == 1.0]
pr_0s = [x for x,l in zip(pr_data, labels) if l == 0.0]
pr_0s = random.sample(pr_0s, len(pr_1s))

print ("sorting sph data...")
sph_data = [x[1] for x in data]
sph_1s = [x for x,l in zip(sph_data, labels) if l == 1.0]
sph_0s = [x for x,l in zip(sph_data, labels) if l == 0.0]
sph_0s = random.sample(sph_0s, len(sph_1s))

print ("sorting srad data...")
srad_data = [x[1] for x in data]
srad_1s = [x for x,l in zip(srad_data, labels) if l == 1.0]
srad_0s = [x for x,l in zip(srad_data, labels) if l == 0.0]
srad_0s = random.sample(srad_0s, len(srad_1s))

print ("sorting th data...")
th_data = [x[1] for x in data]
th_1s = [x for x,l in zip(th_data, labels) if l == 1.0]
th_0s = [x for x,l in zip(th_data, labels) if l == 0.0]
th_0s = random.sample(th_0s, len(th_1s))

print ("sorting tmmn data...")
tmmn_data = [x[1] for x in data]
tmmn_1s = [x for x,l in zip(tmmn_data, labels) if l == 1.0]
tmmn_0s = [x for x,l in zip(tmmn_data, labels) if l == 0.0]
tmmn_0s = random.sample(tmmn_0s, len(tmmn_1s))

print ("sorting tmmx data...")
tmmx_data = [x[1] for x in data]
tmmx_1s = [x for x,l in zip(tmmx_data, labels) if l == 1.0]
tmmx_0s = [x for x,l in zip(tmmx_data, labels) if l == 0.0]
tmmx_0s = random.sample(tmmx_0s, len(tmmx_1s))

print ("sorting vs data...")
vs_data = [x[1] for x in data]
vs_1s = [x for x,l in zip(vs_data, labels) if l == 1.0]
vs_0s = [x for x,l in zip(vs_data, labels) if l == 0.0]
vs_0s = random.sample(vs_0s, len(vs_1s))

features = {'fm100': [fm100_1s, fm100_0s],
            'pet': [pet_1s, pet_0s],
            'pr': [pr_1s, pr_0s],
            'sph': [sph_1s, sph_0s],
            'srad': [srad_1s, srad_0s],
            'th': [th_1s, th_0s],
            'tmmn': [tmmn_1s, tmmn_0s],
            'tmmx': [tmmx_1s, tmmx_0s],
            'vs': [vs_1s, vs_0s],
            }

# plot histogram
for feature in features:
    print("Plotting "+ feature)
    n, bins, patches =plt.hist(features[feature][1], 30, alpha=0.5, color= "blue", label='Non-fire')
    plt.hist(features[feature][0], bins = bins, alpha=0.5, color= "red", label='Fire')
    plt.xlabel(feature+" values")
    plt.ylabel("Number of data points")
    plt.legend()
    plt.show()
    print("done")
    plt.close()
    plt.clf()
    


"""#maxes found from format_arrays_CNN, rounded up
fm100_max = 31
pet_max = 21
pr_max = 172
sph_max = 0.1
srad_max = 400
th_max = 361
tmmn_max = 314
tmmx_max = 327
vs_max = 17"""
