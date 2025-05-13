import pandas as pd
import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Initialize VADER Sentiment Analyzer
sid = SentimentIntensityAnalyzer()

# Load dataset
data = pd.read_csv('cleaned_amazon_reviews.csv')


# Step 1: Analyze Sentiment for Reviews
def analyze_sentiment(text):
    sentiment_score = sid.polarity_scores(text)
    return 1 if sentiment_score['compound'] >= 0.05 else 0  # 1 for positive, 0 for negative


# Apply sentiment analysis to reviews.text column
data['sentiment'] = data['reviews.text'].apply(analyze_sentiment)

# Step 2: Calculate Positive Sentiment Ratio per ASIN
sentiment_summary = data.groupby('asins').agg({
    'sentiment': ['sum', 'count']
}).reset_index()
sentiment_summary.columns = ['asins', 'positive_count', 'total_reviews']
sentiment_summary['positive_ratio'] = sentiment_summary['positive_count'] / sentiment_summary['total_reviews'] * 100

# Filter products with positive ratio > 80%
high_quality_products = sentiment_summary[sentiment_summary['positive_ratio'] > 80]

# Step 3: Integrate TF-IDF for Keyword Matching
# Combine reviews.text into a single string per ASIN
reviews_text_per_asin = data.groupby('asins')['reviews.text'].apply(lambda x: ' '.join(x)).reset_index()

# Merge with high_quality_products to keep only relevant ASINs
tfidf_data = reviews_text_per_asin.merge(high_quality_products[['asins']], on='asins', how='inner')

# Create TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
tfidf_matrix = tfidf.fit_transform(tfidf_data['reviews.text'])

# Compute similarity matrix
similarity_matrix_tfidf = cosine_similarity(tfidf_matrix, tfidf_matrix)


# Step 4: Create Recommendation Function
def get_recommendations(asin, keyword=None, top_n=5):
    if asin not in high_quality_products['asins'].values:
        return [{"error": f"ASIN {asin} not found or has low positive ratio (<80%)."}]

    # Get index of the ASIN in tfidf_data
    asin_idx = tfidf_data[tfidf_data['asins'] == asin].index[0]
    sim_scores = list(enumerate(similarity_matrix_tfidf[asin_idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Exclude the product itself
    sim_scores = [score for score in sim_scores if score[0] != asin_idx][:top_n]

    recommendations = []
    for idx, score in sim_scores:
        rec_asin = tfidf_data.iloc[idx]['asins']
        product_data = data[data['asins'] == rec_asin].iloc[0]
        recommendations.append({
            'asins': rec_asin,
            'name': product_data['name'],
            'categories': product_data['categories'],
            'average_rating': round(product_data['reviews.rating'], 2),
            'positive_ratio': round(
                high_quality_products[high_quality_products['asins'] == rec_asin]['positive_ratio'].iloc[0], 2),
            'similarity_score': round(score, 2)
        })

    # If keyword is provided, filter by keyword relevance
    if keyword:
        keyword_tfidf = tfidf.transform([keyword])
        keyword_sim = cosine_similarity(keyword_tfidf, tfidf_matrix)
        keyword_scores = list(enumerate(keyword_sim[0]))
        keyword_scores = sorted(keyword_scores, key=lambda x: x[1], reverse=True)
        keyword_recommendations = [tfidf_data.iloc[idx]['asins'] for idx, _ in keyword_scores[:top_n]]
        recommendations = [rec for rec in recommendations if rec['asins'] in keyword_recommendations]

    return recommendations[:top_n]


# Step 5: Save Results
sentiment_summary.to_csv('sentiment_summary.csv', index=False)
high_quality_products.to_csv('high_quality_products.csv', index=False)

with open('tfidf_matrix.pkl', 'wb') as f:
    pickle.dump(tfidf_matrix, f)
with open('tfidf_vectorizer.pkl', 'wb') as f:
    pickle.dump(tfidf, f)

# Test the recommendation function
if __name__ == "__main__":
    sample_asin = 'B01AHB9CN2'
    recommendations = get_recommendations(sample_asin, keyword="tablet", top_n=3)
    print("Recommendations for ASIN:", sample_asin)
    for rec in recommendations:
        print(rec)