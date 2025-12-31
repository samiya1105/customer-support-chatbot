import json
import random
import numpy as np
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK data (if not already present)
# We need 'punkt' for tokenization and 'wordnet' for lemmatization
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

class ChatBot:
    def __init__(self, intents_file='intents.json'):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        self.intents = self.load_intents(intents_file)
        self.corpus = []
        self.tags = []
        self.prepare_data()

    def load_intents(self, file_path):
        with open(file_path, 'r') as file:
            intents = json.load(file)
        return intents

    def prepare_data(self):
        # Flatten the data: Create a list of all patterns and their associated tags
        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                self.corpus.append(pattern)
                self.tags.append(intent['tag'])

    def preprocess(self, text):
        # Tokenize and lemmatize (converting to lowercase and trimming whitespace)
        tokens = nltk.word_tokenize(text.lower().strip())
        
        # Remove stop words (like "is", "the", "where", "my", "your") using pre-loaded set
        filtered_tokens = [token for token in tokens if token.isalnum() and token not in self.stop_words]
        
        lemmatized_tokens = [self.lemmatizer.lemmatize(token) for token in filtered_tokens]
        # Return as a string for TF-IDF
        return " ".join(lemmatized_tokens)

    def get_response(self, user_input):
        # Add user input to the corpus temporarily to calculate TF-IDF
        # In a production system, you would fit the vectorizer once and transform new input
        
        # NOTE: For this simple demonstration, re-fitting on every input is inefficient but easy to code.
        # A better way is to fit on the training corpus once. Let's do that.
        
        # Re-doing the fit approach properly:
        # 1. Preprocess the entire corpus
        processed_corpus = [self.preprocess(doc) for doc in self.corpus]
        
        # 2. Vectorize
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(processed_corpus)
        
        # 3. Process user input
        processed_input = self.preprocess(user_input)
        input_vector = vectorizer.transform([processed_input])
        
        # 4. Calculate similarities
        similarities = cosine_similarity(input_vector, tfidf_matrix)
        
        # 5. Find best match
        best_match_index = np.argmax(similarities)
        similarity_score = similarities[0][best_match_index]
        
        if similarity_score < 0.2:
             return "I'm sorry, I didn't verify that. Could you rephrase your question? I can help with store hours, order status, contact details, and returns."
        
        matched_tag = self.tags[best_match_index]
        
        # Return a random response from the matched intent
        for intent in self.intents['intents']:
            if intent['tag'] == matched_tag:
                return random.choice(intent['responses'])
        
        return "I'm confused."
