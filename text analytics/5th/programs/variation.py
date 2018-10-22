from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

# Bring in standard stopwords
stopWords = stopwords.words('english')

print ("\nCalculating document similarity scores...")

# Open and read a bunch of files
doc1=('UCD is a good university to study computer science')
doc2=('I like UCD campus ')
doc3=(' Drink water to lead healthy lifestyle')

# Create a string to use to test the similarity scoring

train_string = 'UCD university are important for nations economy'
# Construct the training set as a list
train_set = [train_string, doc1, doc2, doc3]

# Set up the vectoriser, passing in the stop words
tfidf_vectorizer = TfidfVectorizer(stop_words=stopWords)

# Apply the vectoriser to the training set
tfidf_matrix_train = tfidf_vectorizer.fit_transform(train_set)

# Print the score
print ("\nSimilarity Score [*] ",cosine_similarity(tfidf_matrix_train[0:1], tfidf_matrix_train))