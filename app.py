import streamlit as st
import tempfile

from rag import build_rag_chain


st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="🤖",
    layout="wide"
)


if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "document_loaded" not in st.session_state:
    st.session_state.document_loaded = False


st.title("🤖 AI Document Assistant")
st.caption("Upload a PDF and chat with your documents")


with st.sidebar:

    st.header("📄 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

    if uploaded_file:

        if st.button("Process Document"):

            with st.spinner("Processing PDF..."):

                # Save Uploaded PDF
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as tmp_file:

                    tmp_file.write(uploaded_file.getvalue())
                    pdf_path = tmp_file.name

                # Build Complete RAG Pipeline
                st.session_state.rag_chain = build_rag_chain(
                    pdf_path
                )

                st.session_state.document_loaded = True

            st.success("Document Processed Successfully!")


if not st.session_state.document_loaded:

    st.info(
        "👈 Upload a PDF and click 'Process Document' to begin."
    )

# Display Chat History


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# Chat Input


question = st.chat_input(
    "Ask a question about your document..."
)

#question

if question:

    if not st.session_state.document_loaded:

        st.warning(
            "Please upload and process a PDF first."
        )

        st.stop()

    # User Message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    # Assistant Response

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = st.session_state.rag_chain.invoke(
                question
            )

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )