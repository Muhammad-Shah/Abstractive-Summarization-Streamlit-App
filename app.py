import streamlit as st
from txtai.pipeline import Summary, Textractor
from PyPDF2 import PdfReader


def extract_text_pdf(file_path):
    with open(file=file_path, mode='rb') as f:
        reader = PdfReader(f)
        page = reader.pages[0]
        text = page.extract_text()
    return text


def text_summary(text):
    summary = Summary()
    result = summary((text))
    return result


st.set_page_config(layout='wide')
choice = st.sidebar.selectbox('Select your choice', options=[
                              'Summarize text', 'Summarize document'])
if choice == 'Summarize text':
    st.subheader('Summarize text using textai')
    text_input = st.text_area('Enter your text...')
    if text_input:
        if st.button('Summarize'):
            col_1, col_2 = st.columns([2, 1])
        with col_1:
            st.markdown(body='**Your input text**')
            st.info(body=text_input)
        with col_2:
            st.markdown(body='**Summary**')
            summary = text_summary(text_input)
            st.success(summary)
elif choice == 'Summarize document':
    st.subheader('Summarize document using textai')
    input_file = st.file_uploader(label='Upload Your Document', type=['pdf'])
    if input_file:
        if st.button('Summarize'):
            with open('doc_file.pdf', mode='wb') as f:
                f.write(input_file.getbuffer())
            col_1, col_2 = st.columns([2, 1])
            with col_1:
                st.info('file uploaded successfully')
                extracted_text = extract_text_pdf('doc_file.pdf')
                st.markdown('**Extracted Text is below')
                st.info(extracted_text)
            with col_2:
                st.markdown('**Summary**')
                text = extract_text_pdf('doc_file.pdf')
                summary = text_summary(text)
                st.success(summary)
