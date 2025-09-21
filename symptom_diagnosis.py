class SymptomDiagnosis:
    def diagnose(self, query: str) -> str:
        query = query.lower()
        if "fever" in query or "headache" in query:
            return "You may have a common viral infection. Please consult a doctor if it persists."
        elif "cough" in query or "cold" in query:
            return "You may be experiencing flu or common cold symptoms."
        else:
            return "I need more details about your symptoms."
