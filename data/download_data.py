import kagglehub

# Download the Breast Cancer Wisconsin Dataset
path = kagglehub.dataset_download("uciml/breast-cancer-wisconsin-data")

# Move the dataset to the data/ folder
import shutil
shutil.move(f"{path}/data.csv", "data/data.csv")

print("Dataset downloaded and saved to data/data.csv.")
