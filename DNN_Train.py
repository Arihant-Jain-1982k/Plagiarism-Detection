import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf
from tensorflow import keras 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

tf.compat.v1.enable_eager_execution()

np.random.seed(0)
tf.random.set_seed(0)

X = np.load('Dataset/Plag/X_train.npy')
Y = pd.read_csv("Dataset/Plag/Y_train.csv", index_col = 0)
Y = np.array(Y)
X_test = np.load('Dataset/Plag/X_test.npy')
Y_test = np.load('Dataset/Plag/Y_test.npy')

model = keras.Sequential()
model.add(keras.layers.Dense(10, input_dim = 47158, activation = "relu"))
model.add(keras.layers.Dropout(0.2))
model.add(keras.layers.Dense(1, activation = "sigmoid"))
model.summary()

Adam = keras.optimizers.Adam(learning_rate=0.001, name = 'Adam')

model.compile(loss='binary_crossentropy', optimizer=Adam, run_eagerly=True, metrics=['accuracy'])

history = model.fit(X, Y, batch_size=32, epochs = 20)

results = model.evaluate(X_test, Y_test, batch_size = 32)

plt.plot(np.multiply(history.history['accuracy'], 100), color = 'b')
plt.xlabel("EPOCHS")
plt.ylabel("ACCURACY")
plt.xlim(0, 20)
plt.ylim(0, 100)
plt.grid()
plt.show()