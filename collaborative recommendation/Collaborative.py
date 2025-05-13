import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle
import warnings

warnings.filterwarnings('ignore')

# Load dataset
data = pd.read_csv('cleaned_amazon_reviews.csv')


# Step 1: Preprocess the 'asins' column
# Split multiple ASINs into individual rows while keeping other columns
def split_asins(row):
    asins = row['asins'].split(',')
    return pd.DataFrame({
        'asins': [asin.strip() for asin in asins],
        'name': [row['name']] * len(asins),
        'categories': [row['categories']] * len(asins),
        'reviews.text': [row['reviews.text']] * len(asins),
        'reviews.rating': [row['reviews.rating']] * len(asins)
    })


# Apply the splitting function and concatenate the results
data_expanded = pd.concat([split_asins(row) for _, row in data.iterrows()], ignore_index=True)

# Step 2: Create a product profile
# Group by 'asins' to get product details and average rating
product_profiles = data_expanded.groupby('asins').agg({
    'name': 'first',
    'categories': 'first',
    'reviews.rating': 'mean'  # Average rating for each product
}).reset_index()

# Rename the average rating column for clarity
product_profiles = product_profiles.rename(columns={'reviews.rating': 'average_rating'})

# Step 3: Create an Item-Rating Matrix
# Since we don't have user IDs, we'll use the average rating per product as a feature
item_rating_matrix = product_profiles[['asins', 'average_rating']].set_index('asins')

# Convert the matrix to a 2D numpy array for cosine similarity
item_rating_matrix_values = item_rating_matrix.values

# Step 4: Compute the similarity matrix using cosine similarity
similarity_matrix = cosine_similarity(item_rating_matrix_values)

# Create a DataFrame for the similarity matrix with ASINs as indices and columns
similarity_df = pd.DataFrame(similarity_matrix, index=item_rating_matrix.index, columns=item_rating_matrix.index)

# Step 5: Save the similarity matrix and product profiles for use in Django
with open('similarity_matrix.pkl', 'wb') as f:
    pickle.dump(similarity_df, f)

with open('product_profiles.pkl', 'wb') as f:
    pickle.dump(product_profiles, f)


# Step 6: Define the recommendation function
def get_recommendations(asin, top_n=5):
    """
    Get top N recommended products based on a given ASIN.

    Parameters:
    - asin (str): The ASIN of the product to base recommendations on.
    - top_n (int): Number of recommendations to return.

    Returns:
    - List of dictionaries containing recommended product details.
    """
    if asin not in similarity_df.index:
        return [{"error": f"ASIN {asin} not found in the dataset."}]

    # Get similarity scores for the given ASIN
    sim_scores = similarity_df.loc[asin].sort_values(ascending=False)

    # Exclude the product itself and get the top N similar products
    sim_scores = sim_scores.drop(asin)[:top_n]

    # Get the recommended products' details
    recommendations = []
    for recommended_asin, score in sim_scores.items():
        product = product_profiles[product_profiles['asins'] == recommended_asin].iloc[0]
        recommendations.append({
            'asins': recommended_asin,
            'name': product['name'],
            'categories': product['categories'],
            'average_rating': round(product['average_rating'], 2),
            'similarity_score': round(score, 2)
        })

    return recommendations


# Test the recommendation function
if __name__ == "__main__":
    # Example: Get recommendations for a specific ASIN
    sample_asin = 'B01AHB9CN2'  # Fire HD 8 Tablet
    recommendations = get_recommendations(sample_asin, top_n=3)
    print("Recommendations for ASIN:", sample_asin)
    for rec in recommendations:
        print(rec)