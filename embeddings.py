import numpy as np

def embed(text, dim=50):
    """
    Convert text into a fixed-size numeric vector (embedding)

    Args:
        text (str): input text
        dim (int): size of embedding vector

    Returns:
        numpy array of fixed size
    """

    # Split text into words
    words = text.split()

    # Create empty vector
    vector = np.zeros(dim)

    # Fill vector using hash values
    for i, word in enumerate(words[:dim]):
        vector[i] = hash(word) % 1000  # simple hashing

    # Normalize vector (important for similarity)
    norm = np.linalg.norm(vector)
    if norm != 0:
        vector = vector / norm

    return vector