from drug_info_module import DrugInfo
from first_aid import FirstAid
from symptom_diagnosis import SymptomDiagnosis
from nlp_engine import NLPEngine

# Initialize modules
drug_module = DrugInfo()
first_aid_module = FirstAid()
symptom_module = SymptomDiagnosis()
nlp_engine = NLPEngine()

print("Healthcare Chatbot Prototype 🤖 (type 'exit' to quit)\n")
while True:
    query = input("You: ")
    if query.lower() == "exit":
        print("Bot: Goodbye! Take care. 🩺")
        break

    intent = nlp_engine.get_intent(query)

    if intent == "drug":
        print("Bot:", drug_module.get_info(query))
    elif intent == "firstaid":
        print("Bot:", first_aid_module.get_steps(query))
    elif intent == "disease":
        print("Bot:", symptom_module.diagnose(query))
    else:
        print("Bot: I'm not sure how to respond. Can you rephrase?")
