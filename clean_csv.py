import pandas as pd
import re

# Load the dataset
df = pd.read_csv("malicious_phish.csv")

# Define regex patterns for AWS keys
aws_patterns = [
    r'AKIA[0-9A-Z]{16}',                      # Access Key ID
    r'ASIA[0-9A-Z]{16}',                      # Temporary Access Key ID
    r'(?i)aws.*key.*',                        # Columns like 'aws_secret_key'
    r'(?i).*secret.*key.*',                   # Generic secret key patterns
    r'(?i).*access.*key.*'
]

# Function to detect if any cell matches AWS pattern
def row_has_aws_key(row):
    for cell in row.astype(str):
        for pattern in aws_patterns:
            if re.search(pattern, cell):
                return True
    return False

# Filter rows without AWS keys
clean_df = df[~df.apply(row_has_aws_key, axis=1)]

# Save cleaned dataset
clean_df.to_csv("malicious_phish_clean.csv", index=False)

print("✅ Cleaned dataset saved as 'malicious_phish_clean.csv'.")
print(f"🧹 {len(df) - len(clean_df)} suspicious rows removed.")
