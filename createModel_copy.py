#create model from dataframe
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd

print ("loading files...")
data= pickle.load(open("data/inputs_for_model/allData_df.pickle", "rb"))
x= data[["fm100", "pet", "pr", "sph", "srad", "th", "tmmn", "tmmx", "vs"]]
y= data["fire"]

print("Plotting...")
plt.scatter(data["sph"], data["fire"])
plt.xlabel("input")
plt.ylabel("label")
plt.show()
print("done")

print("Splitting...")
input_train, input_test, labels_train, labels_test = train_test_split(x, y, test_size=0.2)


print ("fitting model...")
model = LinearRegression(fit_intercept = True, normalize = True)
model.fit(input_train, labels_train)

print('Our multiple linear model had an R^2 of: %0.3f' %model.score(input_test, labels_test))

print("Plotting...")
predicted = model.predict(input_test)
plt.plot([0,1],[1,0])
plt.xlabel("Real")
plt.ylabel("Predicted")
plt.scatter(labels_test, predicted)
plt.show()
print("done")

accuracy = metrics.accuracy_score(labels_test, predicted)
print(accuracy)
