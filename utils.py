import streamlit as st
import base64

def set_background(image_file):
    try:
        """
        This function sets the background of a Streamlit app to an image specified by the given image file.

        Parameters:
        image_file (str): The path to the image file to be used as the background.

        Returns:
        None
        """
        with open(image_file, "rb") as f:
            img_data = f.read()
        b64_encoded = base64.b64encode(img_data).decode()
        style = f"""
            <style>
            .stApp {{
                background-image: url(data:image/png;base64,{b64_encoded});
             background-size: cover;
            }}
            </style>
        """
        st.markdown(style, unsafe_allow_html=True)
    except Exception as e:
        raise Exception(e)
    

def role_to_streamlit(role):
    # Check if the role is "model"
    if role == "model":
        # If the role is "model", return "assistant"
        return "assistant"
    else:
        # If the role is not "model", return the role as it is
        return role

