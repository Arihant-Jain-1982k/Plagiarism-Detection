import tensorflow as tf
from tensorflow import keras 
import numpy as np
import matplotlib.pyplot as plt

tf.compat.v1.enable_eager_execution()

np.random.seed(1)
tf.random.set_seed(1)

X = np.load('Dataset/STS/X_train.npy')
Y = np.load('Dataset/STS/Y_train.npy')
Xt = np.load('Dataset/STS/X_test.npy')
Yt = np.load('Dataset/STS/Y_test.npy')
Xd = np.load('Dataset/STS/X_dev.npy')
Yd = np.load('Dataset/STS/Y_dev.npy')

model = keras.Sequential()
model.add(keras.layers.Input((None, 300)))
model.add(keras.layers.LSTM(units = 1, dtype = 'float32', return_sequences=True))
model.add(keras.layers.Dense(units = 20, activation = 'relu'))
model.add(keras.layers.Dense(units = 10, activation = 'relu'))
model.add(keras.layers.Dense(units = 1, activation = 'tanh'))

model.summary()


def custom_loss(y_actual, y_pred):
    y_pred.numpy()
    cosine = keras.losses.CosineSimilarity()
    mid = int(y_pred.shape[1]/2)
    sim = abs(y_actual-cosine(y_pred[:, :mid], y_pred[:, mid:]))
    return sim

def custom_accuracy(y_actual, y_pred):
    y_pred.numpy()
    cosine = keras.losses.CosineSimilarity()
    mid = int(y_pred.shape[1]/2)
    acc = 1 - abs(y_actual-cosine(y_pred[:, :mid], y_pred[:, mid:]))
    return acc


Adam = keras.optimizers.Adam(learning_rate=0.001, name = 'Adam')

model.compile(loss = custom_loss, optimizer = Adam, run_eagerly=True, metrics = custom_accuracy)

history = model.fit(X, Y, batch_size=32, epochs = 100)

result_t = model.evaluate(Xt, Yt)
result_d = model.evaluate(Xd, Yd)

plt.plot(np.multiply(history.history['custom_accuracy'], 100), color = 'b')
plt.xlabel("EPOCHS")
plt.ylabel("ACCURACY")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.grid()
plt.show()