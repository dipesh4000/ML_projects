import streamlit as st
import preprocessor
import helper

st.sidebar.title('Whatsapp chat Analyzer')

uploaded_file = st.sidebar.file_uploader("Choose the file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    #display
    st.dataframe(df)

    user_list = df['user'].unique().tolist()
    user_list.sort()
    user_list.insert(0, 'Overall')

    selected_user = st.sidebar.selectbox("Show analysis for :", user_list)

    if st.sidebar.button("Analyze"):
        num_messages, num_words, num_media_messages = helper.fetch_stats(selected_user, df)
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total Words")
            st.title(num_words)
        with col3:
            st.header("Total Media Messages")
            st.title(num_media_messages)