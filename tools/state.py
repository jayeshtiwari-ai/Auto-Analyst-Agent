class AgentState:

    def __init__(self):

        self.state = {
            "dataset": None,
            "profile": None,
            "summary": None,
            "cleaning_plan": None,
            "cleaned_dataset": None,
            "analysis": None,
            "visualizations": None,
            "insights": None,
            "report": None
        }

    def set(self, key, value):
        self.state[key] = value

    def get(self, key):
        return self.state.get(key)

    def show(self):
        print("\n" + "=" * 60)
        print("AGENT STATE")
        print("=" * 60)

        for key, value in self.state.items():

            if key == "dataset" and value is not None:
                print(f"{key:<20}: Loaded ({value.shape[0]} rows × {value.shape[1]} columns)")

            elif value is None:
                print(f"{key:<20}: ❌")

            else:
                print(f"{key:<20}: ✅")