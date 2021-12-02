import streamlit as st
from utils.help import predict, get_image_download_link

'''
# Image Inpainting #722
'''


'''
___This project's goal was to create a model which would allow one to add colour to old black and white images.___
'''

'''
## Lets see how well our model works 😎

1. Let's take a black and white picture
2. Now we can upload it so that we can feed it to our model
3. What does our model predict? 🤔
'''

'''
## Take a picture and upload it 📷
'''

img_file = st.file_uploader(
    "Please upload your image here",
    ["JPG", "PNG", "JPEG"],
    help="Should not exceed 200MB",
    )

col1, col2 = st.columns(2)

#col1.header("Zones infectées")
if col1.button('Show original'):
    pass
if img_file is not None:
    col1.image(img_file, caption='Original image', use_column_width=True)

#col2.header("Image originale")
if col2.button('Show colourised 🔥'):

    if img_file is not None:

        rgb_img = predict(img_file)
        col2.image(rgb_img, caption='Colourised image', use_column_width=True)
        col2.markdown(get_image_download_link(rgb_img), unsafe_allow_html=True)

    else:
        col2.write(f"Please upload a valid black and white image")
