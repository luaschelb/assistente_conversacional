import os
import streamlit as st
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings

os.environ["GROQ_API_KEY"] = "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"
# Função para carregar documentos PDF
def load_pdfs(uploaded_files):
    docs = []
    for uploaded_file in uploaded_files:
        with open(f"./documentos/{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.getbuffer())
        loader = PyPDFLoader(f"./documentos/{uploaded_file.name}")
        docs.extend(loader.load())
    return docs


# Configuração da interface Streamlit
st.title("Assistente Conversacional baseado em LLM")
uploaded_files = st.file_uploader("Envie arquivos PDF", type="pdf", accept_multiple_files=True)
question = st.text_input("Digite sua pergunta")

if uploaded_files and question:
    docs = load_pdfs(uploaded_files)

    llm = ChatGroq(model="llama3-8b-8192")
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    embedding_function = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(docs, embedding_function)
    retriever = vectorstore.as_retriever()

    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    results = rag_chain.invoke({"input": question})

    st.write("Answer:")
    st.write(results["answer"])