import streamlit as st
import PyPDF2
import openai

#App title
st.title("PDF Chatbot")
st.write("Upload a PDF File, ask questions")

openai.api_key = "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"

#Function extract text from pdf
def extract_text_from_pdf(pdf_file):
    pdf_reader=PyPDF2.PdfReader(pdf_file)
    text=""
    for page_num in range(len(pdf_reader.pages)):
        page=pdf_reader.pages[page_num]
        text+=page.extract_text()
    return text
#Function to generate a response using llm
def generate_response(user_question, pdf_text):
    messages= [
        {"role":"system", "content":"You are an AI assistant tasked with answering questions based on a provided document"},
        {"role":"system", "content":f"Document:{pdf_text}"},
        {"role":"system", "content": user_question}
    ]
    
    #From model response
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=300,
        temperature=0.6, #0 to 1
    )
    return response['choices'][0]['message']['content']

#File uploder for
pdf_file=st.file_uploader("Upload a PDF", type=["pdf"])

if pdf_file is not None:
    pdf_text= extract_text_from_pdf(pdf_file)
    st.write("PDF uploaded successfully")
    
    #Create a form 
    with st.form(key='question_form'):
        user_input=st.text_input("Ask A question about the PDF")
        submit_button= st.form_submit_button(label='Submit')
        
        if submit_button and user_input:
            response=generate_response(user_input, pdf_text)
            st.write("Chatbot Response:")
            st.write(response)


    



