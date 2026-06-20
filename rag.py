from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from prompt import new_prompt
from llm import model

def format_docs(docs):

    return "\n\n".join(
        doc.page_content
        for doc in docs
    )

def build_rag_chain(pdf_path):


    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(
        documents
    )

    embedding = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vector_db = Chroma.from_documents(
        docs,
        embedding
    )

    retriever = vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 3}
    )

    chain = (
        {
            "context":
                retriever | format_docs,
            "question":
                RunnablePassthrough()
        }
        | new_prompt
        | model
        | StrOutputParser()
    )

    return chain