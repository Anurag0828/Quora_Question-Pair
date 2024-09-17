import nltk
from nltk.corpus import stopwords
import pickle

# Download stopwords if not already available
nltk.download('stopwords')

# Fetch stopwords for English
STOP_WORDS = set(stopwords.words('english'))

# Save the stopwords into a new pickle file
with open('stopwords.pkl', 'wb') as f:
    pickle.dump(STOP_WORDS, f)

print("stopwords.pkl has been generated!")
