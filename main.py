import json

def load_faq_data():
    with open("faq.json", "r") as file:
        return json.load(file)

def search_faq(user_question, faq_data):
    user_question = user_question.lower().strip()

    for item in faq_data:
        if user_question == item["question"]:
            return item["answer"]

    return "I do not have enough information. Please contact the mentor."

def log_question(question, answer):
    with open("question_log.txt", "a") as file:
        file.write(f"Question: {question}\n")
        file.write(f"Answer: {answer}\n")
        file.write("---\n")

def main():
    faq_data = load_faq_data()

    print("Welcome to Graduate FAQ Bot")
    print("Ask a question about Python, GCP, VS Code, Git, or Copilot")

    question = input("Enter your question: ")

    answer = search_faq(question, faq_data)
    log_question(question, answer)

    print("Answer:", answer)

main()