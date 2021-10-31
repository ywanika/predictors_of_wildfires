import numpy as np
from sklearn import metrics
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
print ("loading files...")
data = pickle.load(open("data/CNN_model_inputs/masked_arrays/fire.pickle", "rb"))
labels = pickle.load(open("data/CNN_model_inputs/masked_arrays/fm100.pickle", "rb"))

