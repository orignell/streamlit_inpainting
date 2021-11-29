import tensorflow_io as tfio
import tensorflow as tf
import numpy as np
from PIL import Image



def preprocess(rgb_img): #image as array or jpg?

    # resize or alreday done
    # scaled to [0-1] for rgb_to_lab
    # get just l-channel so do [:, :, : 0]
    # get just l channel scaled
    # add dimension of 1 for it to be fed to model
    # l_img = l_img/100
    return None

def predict(rgb_img): # just a bland image

    #tensor of shape (None, 256, 256, 1)
    rgb_img = tf.io.decode_image(rgb_image, dtype=tf.dtypes.uint8) # now image as [0:255]
    # read img as array!!!
    rgb_img =
    # resize or already done
    # scaled to [0-1] for rgb_to_lab
    # get just l-channel so do [:, :, : 0]
    # get just l channel scaled
    # add dimension of 1 for it to be fed to model
    # l_img = l_img/100
    # API call for model that we get off GCP
    # model.predcit(l_img)
    # ouput = a + b
    ab_pred = model.predict(l_img) # WHAT IS MODEL
    # concatenate l + a + b
    l_img = l_img*100 # reversing scaling to original L range [0:100]
    ab_img = ab_pred*127 # if AB[-1:1], reversing scaling to original AB range [-127:127]
    lab_img = tf.concat([l_img, ab_img], axis=3)
    rgb_img = tfio.experimental.color.lab_to_rgb(lab_images)
    rgb_img = tf.image.convert_image_dtype(rgb_img, dtype=tf.uint8) # should be a colour img in RGB [0:255]
    return rgb_img # as tensor? Streamlit like? Prob not
