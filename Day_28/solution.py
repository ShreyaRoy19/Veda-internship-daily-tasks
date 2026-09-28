import pandas as pd
from difflib import SequenceMatcher

# 1. Sample Dataset creation (Replace with pd.read_csv('your_data.csv') in practice)
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['John Smith', 'Jon Smith', 'Alice Johnson', 'Bob Marley', 'John Smith'],
    'email': ['john@example.com', 'john@example.com', 'alice@example.com', 'bob@example.com', 'john.smith@example.com'],
    'city': ['New York', 'New York', 'Chicago', 'Kingston', 'New York']
}

df = pd.DataFrame(data)

# 2. Normalize text data (lowercase, strip whitespace)
def normalize_text(text):
    if isinstance(text, str):
        return text.lower().strip()
    return text

for col in ['name', 'email', 'city']:
    df[col] = df[col].apply(normalize_text)

# 3. Exact Duplicate Report
# Find rows that are exact duplicates based on specific fields (e.g., name, email, city)
exact_duplicates = df[df.duplicated(subset=['name', 'email', 'city'], keep=False)]
print("--- Exact Duplicate Report ---")
print(exact_duplicates if not exact_duplicates.empty else "No exact duplicates found.\n")

# Cleaned dataset removing exact duplicates (keeping the first occurrence)
cleaned_df = df.drop_duplicates(subset=['name', 'email', 'city']).reset_index(drop=True)

# 4. Potential (Near) Duplicate Report using Fuzzy Matching
def similar(a, b):
    return SequenceMatcher(None, str(a), str(b)).ratio()

threshold = 0.8  # Similarity score threshold (80%)
potential_matches = []

for i in range(len(cleaned_df)):
    for j in range(i + 1, len(cleaned_df)):
        name1 = cleaned_df.loc[i, 'name']
        name2 = cleaned_df.loc[j, 'name']
        
        # Check similarity between names
        score = similar(name1, name2)
        if score >= threshold and name1 != name2:
            potential_matches.append({
                'Record_1_ID': cleaned_df.loc[i, 'id'],
                'Record_1_Name': name1,
                'Record_2_ID': cleaned_df.loc[j, 'id'],
                'Record_2_Name': name2,
                'Similarity_Score': round(score, 2)
            })

potential_duplicates_df = pd.DataFrame(potential_matches)

print("\n--- Potential Duplicate Report (Fuzzy Matching) ---")
print(potential_duplicates_df if not potential_duplicates_df.empty else "No potential near-duplicates found.")

# 5. Final Cleaned Dataset output preview
print("\n--- Cleaned Dataset Preview ---")
print(cleaned_df)
