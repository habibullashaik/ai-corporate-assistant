# 🧠 AI Corporate Assistant

A Retrieval-Augmented Generation (RAG) system that lets you query corporate/business PDF documents in natural language — instead of manually searching through pages, just ask.

**🔗 Live Demo:** [document-0871.streamlit.app](https://document-0871.streamlit.app/)
**📄 Full architecture & evaluation notes:** see [`Rag system Audit.docx`](./Rag%20system%20Audit.docx) in this repo

---

## 📌 What It Does

Upload a PDF document and ask questions about its contents in plain English. The system retrieves the most relevant sections of the document and uses an LLM to generate a grounded, context-aware answer — instead of relying on the model's general knowledge alone.

This is useful for:
- Corporate policy documents, SOPs, and internal handbooks
- Long reports and compliance documents
- Any PDF where you need fast, specific answers instead of manual ctrl+F

---

## ⚙️ How It Works

```
PDF Upload → Text Extraction → Chunking → Embeddings (HuggingFace)
     → Stored in ChromaDB → User Query → Similarity Search
     → Relevant Chunks Retrieved → Prompt Construction → LLM Response
```

1. **Document Ingestion** — PDF is parsed and split into manageable chunks
2. **Embedding** — Each chunk is converted into a vector using open-source HuggingFace embedding models (no paid API key required)
3. **Storage & Retrieval** — Vectors are stored in **ChromaDB**; on each query, the most semantically relevant chunks are retrieved
4. **Prompt Engineering** — Retrieved context is injected into a structured prompt to keep the LLM's response grounded in the actual document, reducing hallucination
5. **Generation** — The LLM produces a final answer based only on the retrieved context
6. **Interface** — Everything is wrapped in a simple Streamlit UI and deployed live

---

## 🗂️ Project Structure

| File | Purpose |
|------|---------|
| `app.py` | Streamlit UI — handles file upload, user queries, and displays responses |
| `rag.py` | Core RAG pipeline — chunking, embedding, and retrieval logic via ChromaDB |
| `llm.py` | Handles LLM loading/inference for generating answers |
| `prompt.py` | Prompt templates that structure retrieved context for the LLM |
| `requirements.txt` | Python dependencies |
| `Rag system Audit.docx` | Detailed write-up of the system design, decisions, and evaluation notes |

---

## 🛠️ Tech Stack

- **Language:** Python
- **Embeddings:** HuggingFace (open-source, local — no API key needed)
- **Vector Store:** ChromaDB
- **Frontend/Deployment:** Streamlit
- **Document Type Supported:** PDF

---

## 🚀 Running Locally

```bash
# Clone the repo
git clone https://github.com/habibullashaik/ai-corporate-assistant.git
cd ai-corporate-assistant

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

Then open the local URL Streamlit gives you (usually `http://localhost:8501`) and upload a PDF to start asking questions.

---

## 🧪 What's Next

This is an active, evolving project. Planned next steps:

- [ ] Build a proper **RAG evaluation framework** — measuring retrieval relevance, groundedness, and hallucination rate instead of relying on manual inspection
- [ ] Add support for multiple document types (Word, TXT)
- [ ] Improve chunking strategy for better retrieval accuracy
- [ ] Add conversation memory for multi-turn Q&A

---

## 📬 Connect

Built and maintained by **Habibulla Shaik**, as part of a public learning journey toward becoming a stronger AI Engineer — sharing daily progress on [LinkedIn].

If you find this useful, a ⭐ on the repo is appreciated!
