# python -m streamlit run app.py
import pandas as pd
import streamlit as st
from PIL import Image, ExifTags

def load_image():
    st.sidebar.title("Digital Forensics Tool")
    st.sidebar.subheader("Upload an Image")
    uploaded_file = st.sidebar.file_uploader("Pick an image to test")

    if uploaded_file and st.sidebar.button("Load"):
        image = Image.open(uploaded_file)
        exifdata = image._getexif()

        with st.expander('Selected Image', expanded=True):
            st.image(image, use_column_width=True)

        st.subheader('Image Exchange Information')

        info_dict = {
            "Filename": image.filename,
            "Image Size": image.size,
            "Image Height": image.height,
            "Image Width": image.width,
            "Image Format": image.format,
            "Image Mode": image.mode,
            "Image is Animated": getattr(image, "is_animated", False),
            "Frames in Image": getattr(image, "n_frames", 1)
        }

        for label, value in info_dict.items():
            st.markdown(f"{label:25}: {value}")

        if exifdata:
            for tag_id, data in exifdata.items():
                tag = ExifTags.TAGS.get(tag_id, tag_id)
                if isinstance(data, bytes):
                    data = data.decode()
                st.markdown(f"{tag:25}: {data}")
        else:
            st.markdown('This image does not have metadata!!')

def main():
    load_image()

if __name__ == '__main__':
    main()
