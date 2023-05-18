#Imports
from dotenv import load_dotenv, find_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

#Load API Key
load_dotenv(find_dotenv())
openai_api_key = os.getenv("OPENAI_API_KEY")

#Styling 
st.set_page_config(page_title="Ask your PDF")
st.title("Ask your PDF")

#Instructions
instructions = """
## Instructions
1. Upload a PDF file using the file uploader below.
2. Wait for the system to extract text from your PDF.
3. Once the text is extracted, you can ask questions related to the content of the PDF.
"""
st.markdown(instructions)

pdf = st.file_uploader("Upload your PDF here", type="pdf")

if pdf is not None:

    #Extract Text
    with st.spinner('Extracting text from PDF...'):
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        if text:
            st.success('Text extracted successfully.')
        else:
            st.error('Failed to extract text from the PDF. Please try another file.')

    #Split Text Into Chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    #Embeddings
    with st.spinner('Generating embeddings...'):
        with get_openai_callback() as cb:
            embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)
    st.success('Embeddings generated successfully.')

    #LLM Usage
    question = st.text_input("Ask a question about your PDF")
    if question:
        with st.spinner('Finding answers...'):
            docs = knowledge_base.similarity_search(question)
            llm = OpenAI(model_name="gpt-3.5-turbo")
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=question)

        if response:
            st.markdown(f'## Answer: \n {response}')
            st.download_button("Download Answer", data=response, file_name="answer.txt")
        else:
            st.error('Unable to find an answer to your question. Please try asking in a different way.')
else:
    st.info('Please upload a PDF file.')
