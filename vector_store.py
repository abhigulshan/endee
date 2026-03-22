import numpy as np

database = []

def store_data(id, text, embedding):
    database.append({
        "id": id,
        "text": text,
        "embedding": embedding
    })

def search_data(query_embedding, query_text, top_k=3):
    results = []

    query_words = set(query_text.lower().split())

    for item in database:
        text_words = set(item["text"].lower().split())

        # 🔥 keyword matching score
        common_words = query_words.intersection(text_words)
        keyword_score = len(common_words)

        # 🔥 embedding similarity
        sim = np.dot(query_embedding, item["embedding"])

        total_score = sim + keyword_score * 5   # boost keywords

        results.append((total_score, item))

    results = sorted(results, key=lambda x: x[0], reverse=True)

    return [item[1] for item in results[:top_k]]