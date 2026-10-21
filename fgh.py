from keras.datasets import mnist
from matplotlib import pyplot as plt
(x_train, y_train), (x_test, y_test) = mnist.load_data()



sample_ID = 110

plt.figure(figsize=(2, 2))
plt.imshow(x_train[sample_ID])

plt.title(f"Ground truth label: {y_train[sample_ID]}")
plt.show()