import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Load the dataset
file_path = "bitext_cleaned.csv"
df = pd.read_csv(file_path)

# Initialize VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to label sentiment using VADER
def label_sentiment(text):
    if not isinstance(text, str):
        return "neutral"
    score = analyzer.polarity_scores(text)
    compound_score = score['compound']
    if compound_score >= 0.05:
        return "positive"
    elif compound_score <= -0.05:
        return "negative"
    else:
        return "neutral"

# Apply sentiment labeling to the 'instruction' column
df['sentiment'] = df['instruction'].apply(label_sentiment)

# Prepare data for training
X = df['instruction']
y = df['sentiment']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text to TF-IDF features
tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# Train a Logistic Regression model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# Evaluate the model
y_pred = model.predict(X_test_tfidf)
print("Model Evaluation:")
print(classification_report(y_test, y_pred))

# Save the TF-IDF vectorizer and model
with open('tfidf_vectorizer_user.pkl', 'wb') as f:
    pickle.dump(tfidf, f)
with open('sentiment_model_user.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model and vectorizer saved successfully.")