import tensorflow as tf
import numpy as np
import cv2




def load_image(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def predict(image):
    model = tf.keras.models.load_model("../models/braintumorclassidication.h5")
    classNames = ['Glioma', 'Meningioma', 'Pituitary', 'No tumor']
    image = np.asarray(image)
    image = cv2.resize(image, (224, 224))
    image = image / 255.0  
    image = np.expand_dims(image, axis=0)  
    pred = model.predict(image)
    tumor = classNames[np.argmax(pred[0])]
    return (tumor, pred[0][np.argmax(pred[0])])