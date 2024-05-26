import os
import cv2
import numpy as np 
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout

def load_model():
    mobile_net = tf.keras.applications.MobileNet(input_shape = (224,224,3), include_top=True)
    model = Sequential([
        mobile_net,
        Flatten(),
        Dense(1000, activation='relu'),
        Dense(100, activation='relu'),
        Dense(4, activation='softmax')
    ])
    return model

def load_image(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def predict(image):
    model = load_model() 
    model.load_weights("./models/braintumorclassidication.h5")  
    classNames = ['Glioma', 'Meningioma', 'Pituitary', 'No tumor']
    image = np.asarray(image)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0  
    image = np.expand_dims(image, axis=0)  
    pred = model.predict(image)
    tumor = classNames[np.argmax(pred[0])]
    return (tumor, pred[0][np.argmax(pred[0])])