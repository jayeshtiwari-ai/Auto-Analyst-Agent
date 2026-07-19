def check_dataset(state):

    df = state.get("cleaned_dataset")

    print("\n" + "=" * 60)
    print("FINAL DATASET CHECK")
    print("=" * 60)

    print(df.isnull().sum())