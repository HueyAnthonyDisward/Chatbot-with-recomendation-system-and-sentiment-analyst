import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from pathlib import Path



# Load cleaned Bitext dataset
bitext_data = pd.read_csv('bitext_cleaned.csv')

# Prepare training data
X = bitext_data['instruction']
y = bitext_data['intent']

# Create a pipeline with TfidfVectorizer and LogisticRegression
model = make_pipeline(TfidfVectorizer(), LogisticRegression(max_iter=1000))

# Train the model
model.fit(X, y)

# Save the trained model
joblib.dump(model,'intent_classifier.pkl')
print("Trained intent classifier saved to:",'intent_classifier.pkl')