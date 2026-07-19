from tools import state
from tools.loader import load_dataset
from agents.profiler import profile_dataset
from tools.state import AgentState
from agents.cleaning_advisor import cleaning_advisor
from tools.summary_builder import build_summary
from agents.user_review import user_review
from agents.cleaner import clean_dataset
from agents.checker import check_dataset
from agents.analyzer import analyze_dataset
from agents.visualizer import visualize_dataset
from agents.insight import generate_insights

def main():

    from tools.helper import print_heading

    print_heading("AI Data Scientist Agent")

    path = input("\nEnter CSV file path: ")

    df = load_dataset(path)

    if df is None:
        return

    state = AgentState()

    state.set("dataset", df)

    try:
        profile_dataset(state)
        build_summary(state)
        cleaning_advisor(state)
        user_review(state)
        clean_dataset(state)
        check_dataset(state)
        analyze_dataset(state)
        visualize_dataset(state)
        generate_insights(state)

        
    except Exception as e:
        print(f"Error: {e}")


    state.show()

if __name__ == "__main__":
    main()