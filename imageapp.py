import openai
from PIL import Image
import streamlit as st
from apikey import apikey

# Set API key directly
openai.api_key = apikey

def generate_images(image_description, num_images):
    images = []
    for _ in range(num_images):
        response = openai.Image.create(
            model="dall-e-3",
            prompt=image_description,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        images.append(image_url)
    return images

# Streamlit UI
st.set_page_config(page_title="Image-Generation", page_icon=":camera:", layout="wide")
st.markdown("<h1 style='text-align: center;'>Image-Generation</h1>", unsafe_allow_html=True)
st.subheader("Powered by the most powerful image generation APP")

img_description = st.text_input("Enter a description for the image")
num_of_images = st.number_input("Select the number of images you want to generate", min_value=1, max_value=5, value=1)

if st.button("Generate Images"):
    try:
        generated_images = generate_images(img_description, num_of_images)
        for url in generated_images:
            st.image(url)
    except Exception as e:
        st.error(f"Error generating image: {e}")
