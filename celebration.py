import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from numpy import asarray
st.subheader("1. Click play on this music")

audio_file = open('myaudio.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format="audio/mpeg")

st.subheader("2. Click the button below")
np.random.seed(42)
with st.expander("Yes click here"):

    img = Image.open('Merry Ch.png')

    img = img.convert('1')
    numpydata = asarray(img)

    import pandas as pd

    image = pd.DataFrame(numpydata)

    import seaborn as sns

    # sns.heatmap(image.iloc[500:588,600:1296])

    image_crop= image.iloc[500:588,600:1296]

    image_crop = image_crop.melt(ignore_index=False,var_name="x").reset_index(names=['y'])
    image_crop_text = image_crop[image_crop['value']==False]
    background = image_crop[image_crop['value']==True]

    import matplotlib.pyplot as plt
    fig,ax = plt.subplots(figsize=(12,4))
    frac = st.slider('Try to slide this to the right', 0., 1., 0.,0.01)
    total_data_sampled = pd.concat([background.sample(frac=0.1),image_crop_text.sample(frac=0.5)])
    sns.scatterplot(data = total_data_sampled,x='x',y='y',c='lightgreen',ax=ax)
    sns.scatterplot(data = image_crop_text.sample(frac=frac),x='x',y='y',c='red',ax=ax)
    plt.gca().invert_yaxis()
    st.pyplot(fig)

    if frac>0.18 : 
        st.write("""
        🎄🎅🍴🌟☃️🦌🥰🎄🎅🍴🌟☃️🦌🎄🎅🍴🌟☃️🦌🎄🎅🍴🌟☃️🦌🎄🎅🍴🌟☃️
        Wishing you a joyous and festive Christmas filled with love, laughter, and cherished moments.\n
        May this holiday season bring you warmth, peace, and the company of those you hold dear.\n
        Merry Christmas and may the coming year be filled with happiness and prosperity!\n
        🎄🎅🍴🌟☃️🦌🥰🎄🎅🍴🌟☃️🦌🎄🎅🍴🌟☃️🦌🎄🎅🍴🌟☃️🦌🎄🎅🍴🌟☃️
        """)

st.write("Author : Vinson Ciawandy")
st.write("Date   : 25th December 2023")