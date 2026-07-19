
from urllib import response

from tools import state
from tools.helper import print_error
from tools.llm import ask_llm
import json


def cleaning_advisor(state):

    summary = state.get("summary")

    prompt = f"""
You are a Senior Data Scientist.

Below is the dataset summary.

{summary}

Recommend data cleaning.

Rules:
1. Don't remove rows automatically.
2. Don't remove columns automatically.
3. Explain why.
4. Return ONLY JSON.

Example:

{{
    "Age": {{
        "issue":"Missing Values",
        "recommendation":"Median",
        "reason":"Data may be skewed"
    }}
}}
"""

    response = ask_llm(prompt)
    if response is None:
        print_error("Failed to get cleaning recommendations.")
        return

    print("\nCleaning Recommendation")
    print("=" * 50)
    print(response)
    response = (
    response.replace("```json", "")
            .replace("```", "")
            .strip()
)

    plan = json.loads(response)

    state.set("cleaning_plan", plan)
    

    
    print("\nCleaning Plan Saved Successfully.")