from sentence_transformers import SentenceTransformer
import numpy as np
from scipy.spatial.distance import cosine

# Use a more powerful model
model = SentenceTransformer('all-mpnet-base-v2')

def get_embedding(text):
    return model.encode(text, normalize_embeddings=True)

def semantic_search(documents, meme_description):
    # Generate embeddings
    document_embeddings = model.encode(documents, normalize_embeddings=True)
    meme_embedding = get_embedding(meme_description)
    
    # Compute cosine similarities
    similarities = np.dot(document_embeddings, meme_embedding)
    
    # Find the most similar document
    most_similar_index = np.argmax(similarities)
    return documents[most_similar_index]
