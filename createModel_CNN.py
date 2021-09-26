from keras.datasets import mnist
import numpy as np
from sklearn import metrics
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

print ("loading files...")
data= pickle.load(open("data/inputs_for_model/data_train.pickle", "rb"))
labels = pickle.load(open("data/inputs_for_model/labels_train.pickle", "rb"))

input_train, input_test, labels_train, labels_test = train_test_split(data, labels, test_size=0.2)

