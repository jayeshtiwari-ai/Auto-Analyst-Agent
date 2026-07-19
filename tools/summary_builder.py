def build_summary(state):

    profile = state.get("profile")

    summary = f"""
========================================
DATASET SUMMARY
========================================

Rows : {profile['rows']}
Columns : {profile['columns']}

Numeric Columns
---------------
{", ".join(profile['numeric_columns'])}

Categorical Columns
-------------------
{", ".join(profile['categorical_columns'])}

Missing Values
--------------
"""

    for col, value in profile["missing_values"].items():
        summary += f"{col}: {value}\n"

    summary += f"""

Duplicate Rows
--------------
{profile['duplicate_rows']}
"""

    state.set("summary", summary)

    print(summary)