import pandas as pd

class DrugInfo:
    def __init__(self, file="medicine_corpus.csv"):
        self.data = pd.read_csv(file)

    def get_info(self, query):
        for _, row in self.data.iterrows():
            if row["drug_name"].lower() in query.lower():
                return f"{row['drug_name'].capitalize()} – Usage: {row['usage']}, Dosage: {row['dosage']}, Side Effects: {row['side_effects']}"
        return "Sorry, I don't have information about that medicine."
