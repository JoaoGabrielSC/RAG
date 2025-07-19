# RAG - Retrieval Augmented Generation With Vector DB

This project provides a complete pipeline for extracting text from various document formats (PDF, Word, Images), chunking it, generating embeddings, and storing them in a Vector Database. It is designed to support document-based Retrieval-Augmented Generation (RAG) systems.

## TODO

- [] Implement Services and Repositories to handle database operations (CRUD, queries, etc.)
- [] Add ML Embedding Model to transform raw data into vector embeddings
- [] Add support for multiprocessing or multithreading to concurrently load and process chunked data (ETL load step)
- [] Create the Retrieval API for querying and retrieving vectorized data

## Overview

<img width="1306" height="170" alt="image" src="https://github.com/user-attachments/assets/a6a08df2-2b47-426d-ad00-a9132d4282b8" />

### 🔁 Pipeline Steps (see diagram)

1. **Start** – Begin the document ingestion process.

2. **Send Raw Documents** – Upload raw documents such as PDFs, Word docs, or images.

3. **Text Extractor** – Extract text from different file types using specialized parsers:
   - PDFs → `pdf_text_extractor.py`
   - Images → `image_text_extractor.py` (OCR)

4. **Splitter** – Break extracted text into smaller chunks using a customizable splitter strategy.

5. **Parallel Chunk Processing** – Process chunks in parallel using threads.

6. **Embedding Model** – Convert each chunk into an embedding vector using a pre-trained model.

7. **Vector Database** – Store the resulting embeddings in a vector store for fast retrieval.

## Project Structure

    .
    ├── docker-compose.yaml
    ├── Dockerfile
    ├── examples
    │   ├── image.png
    │   └── volume_tracing.pdf
    ├── LICENSE
    ├── main.py
    ├── Makefile
    ├── mypy.ini
    ├── README.md
    ├── requirements.txt
    └── src
        ├── database
        │   ├── dto
        │   │   ├── __init__.py
        │   │   ├── base_dto.py
        │   │   └── embedding_dto.py
        │   └── models
        │       ├── __init__.py
        │       ├── base.py
        │       └── embedding.py
        ├── entities
        │   └── embedding.py
        ├── repositories
        │   ├── __init__.py
        │   ├── base_repository.py
        │   └── pgvector_repository.py
        ├── services
        │   └── text_extractor
        │       ├── __init__.py
        │       ├── image_text_extractor.py
        │       └── pdf_text_extractor.py
        └── utils
            ├── __init__.py
            └── parser.py

## Installation

```bash
# Clone the repo
git clone git@github.com:JoaoGabrielSC/rag-vectordb.git
cd RAG

# (Optional) Create a virtual environment (using pyenv)
pyenv virtualenv 3.12.9 rag
pyenv activate rag
pyenv local rag

# Install dependencies
pip install -r requirements.txt
```
