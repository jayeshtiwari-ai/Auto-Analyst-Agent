import pandas as pd


def clean_dataset(state):

    df = state.get("dataset").copy()

    plan = state.get("cleaning_plan")

    print("\n" + "=" * 60)
    print("CLEANING DATASET")
    print("=" * 60)
    if plan is None:

        print("No Cleaning Plan Found.")

        return

    for column, details in plan.items():

        recommendation = details["recommendation"].lower()

        if "median" in recommendation:

            df[column] = df[column].fillna(df[column].median())

            print(f"✔ Filled missing values in '{column}' using Median")

        elif "mean" in recommendation:

            df[column] = df[column].fillna(df[column].mean())

            print(f"✔ Filled missing values in '{column}' using Mean")

        elif "mode" in recommendation:

            df[column] = df[column].fillna(df[column].mode()[0])

            print(f"✔ Filled missing values in '{column}' using Mode")

        elif "remove" in recommendation:

            df = df.drop_duplicates()

            print("✔ Duplicate rows removed")


    state.set("cleaned_dataset", df)

    print("\nDataset cleaned successfully.")