import pandas as pd


def profile_dataset(state):

    df = state.get("dataset")

    if df is None:
        print("❌ Dataset not found.")
        return

    # Basic Information
    rows = df.shape[0]
    columns = df.shape[1]

    # Column Types
    numeric_columns = df.select_dtypes(include="number").columns.tolist()
    categorical_columns = df.select_dtypes(exclude="number").columns.tolist()

    # Missing Values
    missing_values = df.isnull().sum().to_dict()

    # Duplicate Rows
    duplicate_rows = int(df.duplicated().sum())

    # Data Types
    data_types = df.dtypes.astype(str).to_dict()

    # Memory Usage
    memory_usage_kb = round(
        df.memory_usage(deep=True).sum() / 1024,
        2
    )

    # Profile Dictionary
    profile = {
        "rows": rows,
        "columns": columns,
        "numeric_columns": numeric_columns,
        "categorical_columns": categorical_columns,
        "missing_values": missing_values,
        "duplicate_rows": duplicate_rows,
        "data_types": data_types,
        "memory_usage_kb": memory_usage_kb
    }

    # Save in State
    state.set("profile", profile)

    print("\n" + "=" * 60)
    print("DATASET PROFILE")
    print("=" * 60)

    print(f"Rows               : {rows}")
    print(f"Columns            : {columns}")
    print(f"Numeric Columns    : {numeric_columns}")
    print(f"Categorical Columns: {categorical_columns}")
    print(f"Duplicate Rows     : {duplicate_rows}")
    print(f"Memory Usage (KB)  : {memory_usage_kb}")

    print("\nMissing Values")
    for col, count in missing_values.items():
        print(f"{col}: {count}")

    print("\nData Types")
    for col, dtype in data_types.items():
        print(f"{col}: {dtype}")

    return profile