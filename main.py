import streamlit as st
from utils.gemini_api import generate_caption

st.set_page_config(page_title="AI Image Captioning App", page_icon="🧠")
st.title("🧠 AI Image Captioning App")
st.markdown("Upload an image and get an AI-generated caption using **Google Gemini Vision Pro**.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        with st.spinner("Generating caption..."):
            caption = generate_caption(uploaded_file)
        st.success("Generated Caption:")
        st.write(caption)
