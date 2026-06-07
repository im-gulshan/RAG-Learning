from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

persistent_directory = "db/chroma_db"

# Load embeddings and vector store
embedding_model = OpenAIEmbeddings(model="text-embedding-3-small")

db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space": "cosine"}  
)

# Search for relevant documents
query = "How did Google's PageRank algorithm differ from traditional search engine ranking methods, and why did it improve search result quality?"

retriever = db.as_retriever(search_kwargs={"k": 5})

# retriever = db.as_retriever(g
#     search_type="similarity_score_threshold",
#     search_kwargs={
#         "k": 5,
#         "score_threshold": 0.3  # Only return chunks with cosine similarity ≥ 0.3
#     }
# )

relevant_docs = retriever.invoke(query)

print(f"User Query: {query}")

# Display results
print("--- Context ---")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")


# Google
# How did Google's PageRank algorithm differ from traditional search engine ranking methods, and why did it improve search result quality?
# Google earns most of its revenue through digital advertising. Explain how Google Ads and AdSense work together to create Google's advertising ecosystem.

# Microsoft
# How did Microsoft's transition from traditional software products to cloud-based services contribute to its growth and market leadership?
# Explain the significance of Microsoft's partnership with OpenAI and how AI capabilities are integrated into products such as Copilot and Azure AI Services.


# NVIDIA
# Why are GPUs more suitable than CPUs for training modern AI and machine learning models?
# What is CUDA, and how did it help NVIDIA expand beyond gaming into artificial intelligence and scientific computing?


# SpaceX
# How did reusable rocket technology change the economics of space exploration, and why is Falcon 9 considered revolutionary?
# What role has SpaceX's partnership with NASA played in the development of Dragon and Crew Dragon spacecraft?


# Tesla
# How have Tesla's battery technology innovations contributed to the widespread adoption of electric vehicles?
# Explain how Tesla uses artificial intelligence in its Autopilot and Full Self-Driving (FSD) systems, and what challenges still exist in achieving full autonomy.

