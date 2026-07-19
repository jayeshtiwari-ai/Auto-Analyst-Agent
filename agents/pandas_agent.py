import pandas as pd


def pandas_agent(state, question):

    df = state.get("cleaned_dataset")

    question = question.lower()

    # --------------------------
    # Rows
    # --------------------------

    if "how many rows" in question:

        return f"The dataset contains {len(df)} rows."

    # --------------------------
    # Columns
    # --------------------------

    if "how many columns" in question:

        return f"The dataset contains {len(df.columns)} columns."

    # --------------------------
    # Missing Values
    # --------------------------

    if "missing" in question:

        missing = df.isnull().sum()

        return missing.to_string()

    # --------------------------
    # Duplicate Rows
    # --------------------------

    if "duplicate" in question:

        return f"There are {df.duplicated().sum()} duplicate rows."

    # --------------------------
    # Numeric Statistics
    # --------------------------

    for col in df.select_dtypes(include="number").columns:

        c = col.lower()

        if c in question:

            if "average" in question or "mean" in question:

                return f"Average {col}: {df[col].mean():.2f}"

            if "highest" in question or "maximum" in question:

                return f"Highest {col}: {df[col].max()}"

            if "lowest" in question or "minimum" in question:

                return f"Lowest {col}: {df[col].min()}"

            if "sum" in question:

                return f"Total {col}: {df[col].sum()}"

    return None