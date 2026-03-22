from embeddings import embed
from vector_store import store_data

def store_memory(text, idx):
    emb = embed(text)
    store_data(f"mem-{idx}", text, emb)