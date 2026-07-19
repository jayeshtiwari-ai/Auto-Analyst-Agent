from tools.llm import ask_llm


def generate_insights(state):

    summary = state.get("summary")
    analysis = state.get("analysis")

    if summary is None:
        print("Dataset summary not found.")
        return

    if analysis is None:
        print("Run Analyzer First.")
        return

    prompt = f"""
You are an expert Senior Data Scientist.

You are analysing a cleaned dataset.

================================================

DATASET SUMMARY

{summary}

================================================

STATISTICS

{analysis['statistics']}

================================================

CORRELATION

{analysis['correlation']}

================================================

MISSING VALUES

{analysis['missing_values']}

================================================

Write a professional report in the following format.

# Executive Summary

Write 4-5 lines.

# Top 5 Key Insights

Use bullet points.

# Business Recommendations

Give 5 practical recommendations.

Keep the language simple and professional.
"""

    insights = ask_llm(prompt)

    state.set("insights", insights)

    print("\n" + "=" * 60)
    print("AI INSIGHTS")
    print("=" * 60)
    print(insights)