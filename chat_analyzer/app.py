import streamlit as st

st.sidebar.title('Whatsapp chat Analyzer')

uploaded_file = st.sidebar.file_uploader("Choose the file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)