import os
import matplotlib.pyplot as plt
import seaborn as sns


def visualize_dataset(state):

    df = state.get("cleaned_dataset")

    if df is None or df.empty:
        print("Dataset is empty.")
        return

    os.makedirs("outputs", exist_ok=True)

    print("\nGenerating Charts...")

    sns.set_style("whitegrid")

    # ==========================================================
    # Missing Values
    # ==========================================================

    missing = df.isnull().sum()
    missing = missing[missing > 0]

    if not missing.empty:

        plt.figure(figsize=(5, 3))

        missing.sort_values(ascending=False).plot(
            kind="bar",
            color="tomato"
        )

        plt.title("Missing Values")
        plt.xlabel("")
        plt.ylabel("Count")

        plt.tight_layout()

        plt.savefig(
            "outputs/missing_values.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    else:

        if os.path.exists("outputs/missing_values.png"):
            os.remove("outputs/missing_values.png")

    # ==========================================================
    # Correlation Heatmap
    # ==========================================================

    numeric_df = df.select_dtypes(include="number")

    if len(numeric_df.columns) >= 2:

        plt.figure(figsize=(5, 4))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            cmap="Blues",
            fmt=".2f",
            linewidths=0.5
        )

        plt.title("Correlation")

        plt.tight_layout()

        plt.savefig(
            "outputs/correlation_heatmap.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    # ==========================================================
    # Histogram
    # Skip ID columns
    # ==========================================================

    histogram_column = None

    for col in numeric_df.columns:

        if "id" not in col.lower():

            histogram_column = col
            break

    if histogram_column:

        plt.figure(figsize=(5, 3))

        sns.histplot(
            df[histogram_column],
            bins=20,
            kde=True,
            color="steelblue"
        )

        plt.title(f"{histogram_column} Distribution")

        plt.xlabel(histogram_column)

        plt.tight_layout()

        plt.savefig(
            "outputs/distribution.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    # ==========================================================
    # Box Plot
    # ==========================================================

    if histogram_column:

        plt.figure(figsize=(5, 3))

        sns.boxplot(
            x=df[histogram_column],
            color="skyblue"
        )

        plt.title(f"{histogram_column} Box Plot")

        plt.tight_layout()

        plt.savefig(
            "outputs/boxplot.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    # ==========================================================
    # Category Chart
    # ==========================================================

    categorical_df = df.select_dtypes(
        include=["object", "category"]
    )

    if len(categorical_df.columns):

        column = categorical_df.columns[0]

        counts = df[column].value_counts()

        plt.figure(figsize=(5, 3))

        if len(counts) <= 5:

            counts.plot(
                kind="pie",
                autopct="%1.1f%%",
                ylabel=""
            )

            plt.title(column)

        else:

            counts.head(10).plot(
                kind="bar",
                color="royalblue"
            )

            plt.title(column)

            plt.ylabel("Count")

        plt.tight_layout()

        plt.savefig(
            "outputs/categories.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    print("✅ Charts Generated Successfully")