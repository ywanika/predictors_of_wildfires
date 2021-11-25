import numpy as np
from sklearn import metrics
import pickle
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
print ("loading files...")
data = pickle.load(open("data/CNN_model_inputs/input_arrays/images.pickle", "rb"))
labels = pickle.load(open("data/CNN_model_inputs/input_arrays/labels.pickle", "rb"))

#convert to array
data = np.asarray(data)
labels = np.asarray(labels)

#create train and test data, train.shape = (3364, 24, 24, 9) test.shape= (842, 24, 24, 9)
inputs_train, inputs_test, labels_train, labels_test = train_test_split(data, labels, test_size=0.2, random_state=1)

#create model
model = Sequential()
#add layers
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(24, 24, 9)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(256, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='softmax'))

#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#train the model
history = model.fit(inputs_train, labels_train, epochs=10, 
                    validation_data=(inputs_test, labels_test))

plt.plot(history.history['acc'], label='acc')
plt.plot(history.history['val_acc'], label = 'val_acc')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0, 1])
plt.legend(loc='lower right')
plt.show()