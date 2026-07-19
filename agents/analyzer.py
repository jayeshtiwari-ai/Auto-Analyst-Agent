import pandas as pd


def analyze_dataset(state):

    df = state.get("cleaned_dataset")

    print("\n" + "=" * 60)
    print("DATA ANALYSIS")
    print("=" * 60)

    analysis = {}

    # Basic Information
    analysis["rows"] = df.shape[0]
    analysis["columns"] = df.shape[1]

    # Numerical Statistics
    analysis["statistics"] = df.describe().to_dict()

    # Correlation
    analysis["correlation"] = (
        df.select_dtypes(include="number")
        .corr()
        .round(2)
        .to_dict()
    )

    # Missing Values
    analysis["missing_values"] = df.isnull().sum().to_dict()

    state.set("analysis", analysis)
    df = state.get("cleaned_dataset")

    if df is None:

        print("Dataset not cleaned yet.")

        return

    print("✅ Analysis Completed")
    print("\nRows :", analysis["rows"])
    print("Columns :", analysis["columns"])

    print("\nMissing Values")
    print(analysis["missing_values"])