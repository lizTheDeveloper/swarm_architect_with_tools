# Python function to classify a resource based on a summary
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# The function assumes 'curriculum_tree' is a list of folder names
# and 'summary' is the text summary of the resource

def classify_resource(curriculum_tree, summary):
    # Include the summary as part of the documents to assess
    documents = curriculum_tree + [summary]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

    # Calculate similarity scores
    cosine_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    folder_index = cosine_scores.argmax()

    # Return the folder with the highest similarity score
    return curriculum_tree[folder_index]
