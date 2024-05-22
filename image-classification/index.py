#  i need to build a CNN model to classify a set of images into either of two classes. Do it with python


# Importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Loading the dataset
train_data = ImageDataGenerator(
    rescale=1.0 / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True
)
test_data = ImageDataGenerator(rescale=1.0 / 255)

train_set = train_data.flow_from_directory(
    "dataset/training_set", target_size=(64, 64), batch_size=32, class_mode="binary"
)
test_set = test_data.flow_from_directory(
    "dataset/test_set", target_size=(64, 64), batch_size=32, class_mode="binary"
)

# Building the CNN model

model = Sequential()
# convolution
model.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation="relu"))
# pooling
model.add(MaxPooling2D(pool_size=(2, 2)))
# convolution
model.add(Conv2D(32, (3, 3), activation="relu"))
# pooling
model.add(MaxPooling2D(pool_size=(2, 2)))
# flattening
model.add(Flatten())
# full connection
model.add(Dense(units=128, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(units=1, activation="sigmoid"))

# Compiling the model
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Training the model
model.fit(
    train_set,
    steps_per_epoch=8000,
    epochs=25,
    validation_data=test_set,
    validation_steps=2000,
)

# Making predictions
import numpy as np
from tensorflow.keras.preprocessing import image

test_image = image.load_img(
    "dataset/single_prediction/cat_or_dog_1.jpg", target_size=(64, 64)
)
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
result = model.predict(test_image)
train_set.class_indices
if result[0][0] == 1:
    prediction = "dog"
else:
    prediction = "cat"
print(prediction)
