import numpy as np
import pickle
import matplotlib.pyplot as plt
import random

print ("loading files...")
data= pickle.load(open("data/inputs_for_model/data_train.pickle", "rb"))
labels = pickle.load(open("data/inputs_for_model/labels_train.pickle", "rb"))


fm100_data = [x[0] for x in data]
fm100_1s = [x for x,l in zip(fm100_data, labels) if l == 1.0]
fm100_0s = [x for x,l in zip(fm100_data, labels) if l == 0.0] # lis of fm100 vals of no fire
fm100_0s = random.sample(fm100_0s, len(fm100_1s))

# plot histogram
plt.hist(fm100_1s, label='Fire')
plt.hist(fm100_0s, label='Non-fire')
plt.legend()
plt.show()

print("hi")



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

#features = ['fm100', 'pet', 'pr', 'sph', 'srad', 'th', 'tmmn', 'tmmx', 'vs']

"""for i, name in enumerate(features):
    print("Plotting"+ name)
    plt.xlabel(name+ "val")
    plt.ylabel("fire?")
    plt.scatter(data[:][i], labels)
    print("show")
    plt.show()
    print("done")"""

    #[ x[0] for x in a]
"""fm100 = [ x[0] for x in data]

print("Plotting fm100")
plt.xlabel("fm100 val")
plt.ylabel("fire?")
plt.scatter(fm100, labels)
print("show")
plt.show()
print("done")"""