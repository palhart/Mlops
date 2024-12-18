from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load LLaMA tokenizer and model
model_name = "meta/llama-3.2.1b"  # Replace with the correct Hugging Face model path or local model path
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Function to get embeddings from LLaMA
def get_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
    # Use the mean of the token embeddings (last hidden state) for the final embedding
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return embeddings

# Semantic search function
def semantic_search(documents, meme_description):
    # Generate embeddings for documents and meme description
    document_embeddings = np.array([get_embedding(doc) for doc in documents])
    meme_embedding = get_embedding(meme_description).reshape(1, -1)
    
    # Compute cosine similarities
    similarities = cosine_similarity(document_embeddings, meme_embedding).flatten()
    
    # Rank results
    ranked_indices = np.argsort(similarities)[::-1]
    ranked_results = [(documents[i], similarities[i]) for i in ranked_indices]
    return ranked_results
