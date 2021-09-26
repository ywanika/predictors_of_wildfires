import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import pickle

print ("loading files...")
data_train = pickle.load(open("data/inputs_for_model/data_train.pickle", "rb")) #[20][365/6, 238, 278]
labels_train = pickle.load(open("data/inputs_for_model/labels_train.pickle", "rb")) #[20][365/6, 238, 278]

print ("fitting model...")
model = LinearRegression()
model.fit(data_train, labels_train)

print('Our multiple linear model had an R^2 of: %0.3f' %model.score(data_train, labels_train))

#y_pred = model.predict(inputs_test)
#accuracy = metrics.accuracy_score(labels_test, y_pred)
#print(accuracy)
