import os
import pandas as pd


def load_dataset(path):

    if not os.path.exists(path):
        print(f"\n❌ File not found: {path}")
        return None

    try:

        df = pd.read_csv(path)

        print("\n✅ Dataset Loaded Successfully!")
        print(f"Shape : {df.shape}")

        return df

    except Exception as e:

        print("\n❌ Error loading dataset")
        print(e)

        return None