import streamlit as st
import requests
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from utils.test import addition

'''
# Image In-Painting
'''

'''
___This project's goal was to create a model which would allow one to add colour to old black and white images.___
'''

'''
## Lets see how well our model works 😎

1. Let's take a black and white picture of one of us
2. Then we can upload it so that we can feed it to our model
3. What does our model predict
4. Can you guess which image is the fake one? 🤔
'''

'''
## Take a picture and upload it 📷
'''

bw_img = st.file_uploader("Please upload your image here, make sure it does not exceed 200MB.", ["jpg", "png"], help="Help", )


'''
___Need to convert uploaded jpg to RGB data format so that we can pass it to the generator___
'''

#converting image to tensor


im = None
np_img = None

if st.button('click me'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    if bw_img is not None:
        st.write('I was clicked 🎉')
        im = Image.open(bw_img)
        np_img = np.array(im)
        st.write(f'The type of bw_img: {type(bw_img)}')
    else:
        st.write(f"Please upload a valid black and white image")


'''
Streamlit does not seem to like tensorflow!!!
Nor numpy?
'''

if st.button('Show input image'):
    st.write(f"A ghost says {addition()}")
    st.image(bw_img, caption='Test', use_column_width=False)
    fig, ax = plt.subplots()
    face = np_img
    ax.imshow(face, cmap='gray')
    st.pyplot(fig)
