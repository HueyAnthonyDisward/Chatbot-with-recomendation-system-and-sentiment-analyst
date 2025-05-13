import pandas as pd
# Load dataset
data = pd.read_csv('1429_1.csv')  # Adjust path

# Step 1: Clean data
# Keep 'asins' column along with other relevant columns
data = data[['asins', 'name', 'categories', 'reviews.text', 'reviews.rating']].dropna()
data = data.drop_duplicates()

# Step 2: Extract categories (assuming 'categories' column exists)
# If categories are in a list format (e.g., "[Electronics, Headphones]"), parse them
data['categories'] = data['categories'].str.strip('[]').str.split(',').str[0]  # Take the first category
category_counts = data['categories'].value_counts()
print("Category counts:")
print(category_counts)

# Step 3: Select top 10 categories
top_10_categories = category_counts.head(10).index.tolist()
print("\nSelected 10 categories:")
print(top_10_categories)

# Filter data for selected categories
filtered_data = data[data['categories'].isin(top_10_categories)]

# Step 4: Save cleaned data
filtered_data.to_csv('cleaned_amazon_reviews.csv', index=False)
print("Cleaned data saved with 10 categories!")