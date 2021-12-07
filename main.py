import tensorflow as tf
import tensorflow_hub as hub
import cv2
import numpy as np
from os import remove, listdir
from os.path import isfile, join

import nanocamera as nano

PATH = 'path\\to\\model' # put the path to the trained model file here, should be stored on the jetson nano
model = tf.keras.models.load_model(PATH, custom_objects={'KerasLayer' : hub.KerasLayer})
labels = ['CHICKEN NUGGETS', 'CHICKED PATTIES', 'HASH BROWNS', 'SHOESTRING FRIES']

# MAIN LOOP
while(1):
    while not((cv2.waitKey(25) & 0xFF) == ord('q')): # while q is not pressed, use q to take a picture
       continue

    #Take picure
    camera = nano.Camera(flip=2, width=640, height=480, fps=30)
    image = camera.read()

    # opencv reads images in BGR, but the model needs RGB images, therefore we have to convert the color scheme
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # clear the camera for memory purposes
    camera.release()
    del camera

    # make prediction and get label id
    prediction = model.predict(img)
    prediction_id = np.argmax(prediction, axis=-1)

    # get the output prediction
    out_pred = labels[prediction_id]

    # display output prediction and confirm proper food selected
    print("Model Prediction:", out_pred)

    print("Continue operation? (y/n)")
    selection = input('>> ')

    if selection.lower() == 'y':
        print("Commencing frying process.")
