from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class NLPEngine:
    def __init__(self):
        # Tiny demo dataset
        X = [
            "I have fever and headache",
            "Give me details about paracetamol",
            "What are the side effects of ibuprofen?",
            "How to treat a cut on my hand?",
            "Tell me about aspirin",
            "What to do in case of burns?",
        ]
        y = ["disease", "drug", "drug", "firstaid", "drug", "firstaid"]

        self.vectorizer = TfidfVectorizer()
        X_vec = self.vectorizer.fit_transform(X)

        self.model = LogisticRegression()
        self.model.fit(X_vec, y)

    def get_intent(self, query: str) -> str:
        return self.model.predict(self.vectorizer.transform([query]))[0]
