import pandas as pd
from pathlib import Path


# Load Bitext dataset
bitext_data = pd.read_csv('Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv')

# Step 1: Check unique values in 'category' and 'intent'
print("Categories:", bitext_data['category'].unique())
print("Intents:", bitext_data['intent'].unique())

# Step 2: Filter data
# Only keep rows where category is related to e-commerce (adjust based on actual categories)


# Drop rows with missing instruction, intent, or response
bitext_data = bitext_data.dropna(subset=['instruction', 'intent', 'response'])

# Drop the 'flags' column as it's not needed
bitext_data = bitext_data.drop(columns=['flags'])

# Step 3: Normalize data
# Convert 'intent' to lowercase to avoid duplicates
bitext_data['intent'] = bitext_data['intent'].str.lower()
# Ensure 'instruction' and 'response' are strings
bitext_data['instruction'] = bitext_data['instruction'].astype(str)
bitext_data['response'] = bitext_data['response'].astype(str)

# Step 4: Save the cleaned dataset
bitext_data.to_csv('bitext_cleaned.csv', index=False)
print("Cleaned Bitext dataset saved to:",'bitext_cleaned.csv')