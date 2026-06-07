# RAG Learning

This project is a beginner-friendly Retrieval-Augmented Generation (RAG) example built with Python.

## What this project does
- Loads documents from the `docs/` folder
- Creates embeddings and stores them in a local vector database
- Retrieves relevant context for user queries
- Demonstrates a simple RAG pipeline

## Files
- `ingestion_pipeline.py` — processes and stores documents
- `retrieval_pipeline.py` — performs retrieval and query answering
- `docs/` — sample documents used for the RAG example

## Setup
1. Create and activate a virtual environment
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the ingestion pipeline:
   ```bash
   python ingestion_pipeline.py
   ```
4. Run the retrieval pipeline:
   ```bash
   python retrieval_pipeline.py
   ```

## Notes
- Make sure your environment variables are set correctly if the project uses them.
- The local database is stored under `db/`.

## License
This project is for learning and experimentation purposes.
