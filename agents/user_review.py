import json


def user_review(state):

    plan = state.get("cleaning_plan")

    try:
        plan = json.loads(plan)

    except Exception:
        print("Invalid JSON received from LLM.")
        return

    print("\n" + "=" * 60)
    print("AI CLEANING RECOMMENDATIONS")
    print("=" * 60)

    final_plan = {}

    for column, details in plan.items():

        print(f"\nColumn : {column}")
        print(f"Issue  : {details['issue']}")
        print(f"Suggested : {details['recommendation']}")
        print(f"Reason : {details['reason']}")

        choice = input("\nApply this recommendation? (Y/N): ").upper()

        if choice == "Y":
            final_plan[column] = details

        else:
            print("Skipped.")

    state.set("cleaning_plan", final_plan)
    print("\nFinal Cleaning Plan Saved Successfully.")