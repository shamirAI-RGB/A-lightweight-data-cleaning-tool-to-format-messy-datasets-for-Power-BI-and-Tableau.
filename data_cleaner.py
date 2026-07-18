import pandas as pd

def clean_data(file_path):
    # Membaca fail data
    print(f"Loading dataset from {file_path}...")
    df = pd.read_csv(file_path)
    
    # Membuang baris yang mempunyai nilai kosong (null)
    print("Removing null values...")
    df_cleaned = df.dropna()
    
    # Membuang data yang berulang (duplicates)
    print("Removing duplicates...")
    df_cleaned = df_cleaned.drop_duplicates()
    
    print("Data is cleaned and ready for dashboard visualization!")
    return df_cleaned

if __name__ == "__main__":
    print("Simple Data Prep Tool Started.")
