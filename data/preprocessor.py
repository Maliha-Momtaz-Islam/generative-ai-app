import pandas as pd

# Load the dataset
data = pd.read_csv("data/data.csv")

# Convert rows to text summaries
def row_to_text(row):
    text = (
        f"This sample has a radius mean of {row['radius_mean']}, "
        f"texture mean of {row['texture_mean']}, "
        f"and perimeter mean of {row['perimeter_mean']}. "
        f"The diagnosis is {'malignant' if row['diagnosis'] == 'M' else 'benign'}."
    )
    return text

# Apply the function to each row
data['text'] = data.apply(row_to_text, axis=1)

# Save as a text file
with open("data/training_data.txt", "w") as f:
    for text in data['text']:
        f.write(text + "\n\n")

print("training_data.txt has been created in the data/ folder.")
