import pandas as pd

# Load the complete dataset
input_file = r"C:\Users\cheta\Desktop\pre sih\training data\onelakh.csv"

df = pd.read_csv(input_file)

# Round all numeric columns to 3 decimal places
numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].round(3)

# Save the complete processed dataset
output_file = r"C:\Users\cheta\Desktop\pre sih\training data\onelakh1.csv"

df.to_csv(output_file, index=False)

# Display first 5 rows
print("Processed dataset:")
print(df.head())

print("\nOriginal shape:", df.shape)
print("Saved successfully to:")
print(output_file)