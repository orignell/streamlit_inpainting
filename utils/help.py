import numpy as np
from PIL import Image
import requests
import json
import base64


def predict(img_file):  #uploaded as PIL object

    img = Image.open(img_file)
    img = img.convert('RGB')
    og_img_array = np.array(img)
    og_height, og_width, og_channel = og_img_array.shape    # storing the original shape for later
    resized_img = img.resize((256, 256))
    img_array = np.array(resized_img)                       # img now an array of size (256, 256, 3)
    img_array = img_array.astype('uint8')                   # img now in [0:255]
    height, width, channel = img_array.shape  # the dimesnsions for preproc
    img_1d_array = img_array.reshape(height * width * channel)
    img_enc = base64.b64encode(img_1d_array)                # this is the image in one line
    img_enc = img_enc.decode('utf8').replace("'", '"')      # readable by api now

    # sending the api request
    headers = {}
    headers['Content-Type'] = 'application/json'
    request_dict = {'image' : img_enc, 'height' : height, 'width' : width, 'channel' : channel}
    result = requests.post(
        'https://imageinpainting-prh3yqxaha-ew.a.run.app/predict',
        json.dumps(request_dict),
        headers=headers)
    result = result.json()
    decoded_string = base64.b64decode(bytes(result['image'], 'utf-8'))
    img = np.frombuffer(decoded_string, dtype='uint8')
    img = img.reshape((result['height'], result['width'], result['channel']))

    # we now have a colorised images in (256, 256, 3), we want it in original format
    rgb_img = Image.fromarray(img)
    rgb_img = rgb_img.resize((og_width, og_height))

    return rgb_img
