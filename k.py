from keras import Sequential, Input
from keras.src.layers import Dense

model = Sequential([
    Input(shape=(3, )),
    Dense(units=4),
    Dense(units=4),
    Dense(units=1),
])
model.summary()