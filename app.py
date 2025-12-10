import streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image

# Load model once at the top
with open('rfc.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Forest Cover Type Prediction")
st.write("This app predicts the forest cover type based on cartographic variables.")

st.write("Enter all cover type features as comma-separated values (in the same order as training data).")

user_input = st.text_input('Features (comma-separated)')

# Define mapping for cover types
cover_type_dict = {
    1: {'cover_image': 'img_1.png', 'description': 'Spruce/Fir'},
    2: {'cover_image': 'img_2.png', 'description': 'Lodgepole Pine'},
    3: {'cover_image': 'img_3.png', 'description': 'Ponderosa Pine'},
    4: {'cover_image': 'img_4.png', 'description': 'Cottonwood/Willow'},
    5: {'cover_image': 'img_5.png', 'description': 'Aspen'},
    6: {'cover_image': 'img_6.png', 'description': 'Douglas-fir'},
    7: {'cover_image': 'img_7.png', 'description': 'Pine'}
}

if user_input:
    try:
        # Split and convert to float (model expects numeric)
        input_list = [float(x.strip()) for x in user_input.split(',')]
        input_array = np.array(input_list).reshape(1, -1)

        # Predict
        prediction = model.predict(input_array)
        pred_class = int(prediction[0])

        st.write(f'**Predicted forest cover type:** {pred_class}')

        # Show image & description
        cover_info = cover_type_dict.get(pred_class, None)
        if cover_info is not None:
            image = Image.open(cover_info['cover_image'])
            st.image(image, caption=cover_info['description'])
        else:
            st.write("No additional information available for this cover type.")

    except Exception as e:
        st.error(f"Error while predicting: {e}")
        st.info("Make sure you entered the correct number of numeric features, separated by commas.")
