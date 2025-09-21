import pandas as pd

class FirstAid:
    def __init__(self, file="first_aid_corpus.csv"):
        self.data = pd.read_csv(file)

    def get_steps(self, query: str) -> str:
        for _, row in self.data.iterrows():
            if row["condition"].lower() in query.lower():
                return f"First Aid for {row['condition'].capitalize()}: {row['steps']}"
        return "Please provide more details about the situation."
