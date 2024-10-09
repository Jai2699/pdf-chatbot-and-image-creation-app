from openai import OpenAI  # openai 1.51.0
from PIL import Image
import streamlit as st
from apikey import apikey
#Initialize your image generation client
client=OpenAI(api_key=apikey)

def generate_images(image_description, num_images):
    images=[] #
    for i in range(num_images):#
        
        img_response=client.images.generate(
            model="dall-e-3",
            prompt=image_description,
            size='1024x1024',
            quality='standard',
            n=1
        )
        image_url= img_response.data[0].url#
        images.append(image_url)#
    return images#
st.set_page_config(page_title="Image-Generation", page_icon=":camera:",layout="wide")
#create a title
# st.title("Image-Generation")
st.markdown("<h1 style='text-align: center;'>Image-Generation</h1>", unsafe_allow_html=True)
#Create a subheader
st.subheader("Powered by the most powerful image generation APP")
img_description=st.text_input("Enter a description for the image")
num_of_images=st.number_input("Select the number of images you want to generate",min_value=1, max_value=5, value=1)

#create button
if st.button("Generate Images"):
    generate_image=generate_images(img_description, num_of_images)#
    
    for i in range(len(generate_image)):#
        st.image(generate_image[i])#
