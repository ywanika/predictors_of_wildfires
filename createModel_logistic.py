import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

print ("loading files...")
data= pickle.load(open("data/inputs_for_model/data_train.pickle", "rb"))
labels = pickle.load(open("data/inputs_for_model/labels_train.pickle", "rb"))

input_train, input_test, labels_train, labels_test = train_test_split(data, labels, test_size=0.2)

print ("fitting model...")
model = LogisticRegression()
model.fit(input_train, labels_train)

print("Saving model...")
filename = 'model.sav'
pickle.dump(model, open(filename, 'wb'))

print('Our multiple linear model had an R^2 of: %0.8f ' %model.score(input_test, labels_test))

"""
print ("loading files...")
data= pickle.load(open("data/inputs_for_model/data_train.pickle", "rb"))
labels = pickle.load(open("data/inputs_for_model/labels_train.pickle", "rb"))

input_train, input_test, labels_train, labels_test = train_test_split(data, labels, test_size=0.2)

print("Loading model...")
filename = 'model.sav'
model = pickle.load(open(filename, 'rb'))
"""

print("Plotting...")
predicted = model.predict(input_test)
print (predicted)
plt.plot([0,1],[1,0])
plt.xlabel("Real")
plt.ylabel("Predicted")
plt.scatter(labels_test, predicted)
plt.show()
print("done")