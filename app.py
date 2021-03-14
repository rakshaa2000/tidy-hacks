import streamlit as st
import torch
import torchvision
from PIL import Image
import os
import pickle as pkle
import cv2 as cv
from keras.preprocessing.image import load_img
from collections import OrderedDict

def predict(img):
    model.load("model.pth")
    clean_status,acc=model.predict(img)
    return (clean_status,acc)
def main():
    page_bg_img = '''
    <style>
    html {
    background-image: url('https://firebasestorage.googleapis.com/v0/b/offisca-2d74b.appspot.com/o/Desktop%20-%204.svg?alt=media&token=683be8ed-89bc-474d-aa00-4b005c198e0c');
    background-size: cover;


    }
    </style>
    '''

    st.markdown(page_bg_img, unsafe_allow_html=True)
   

    
    text_by_img=''' <a>Hello</a>
    <style>
    a{
        font-weight:bold;
    }
    '''
    st.title("Upload")

    uploaded_file = st.file_uploader("Choose an image...", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        img_show='''<img width= "800px" height="300px" src={image} text-align='center'></img>
        '''
        st.image(image, caption='Uploaded Image.', width=300 )
        st.write("")
        label,tagline=predict(image)
        st.write("Messiness Index: "+ str(label)+'/10')
        st.write(tagline)
      
if __name__=="__main__":
    main()


