import json
import csv
import time
import logging
import os

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Check for required files
if not os.path.exists('questions.json'):
    logging.error("Missing questions.json file.")
    print("⚠️ Quiz file not found!")
    exit()

# Load quiz questions from JSON
with open('questions.json', 'r') as f:
    try:
        questions = json.load(f)
    except json.JSONDecodeError as e:
        logging.error("Error loading JSON: %s", e)
        print("⚠️ Error reading quiz file.")
        exit()

logging.info("Quiz started.")
print("\nQuiz started time running out🕐")
print("Answer the following questions:\n")

# ------------------ QUIZ LOOP ------------------
results = []

for q in questions:
    print(f"👉 {q['question']}")
    start = time.time()
    user_answer = input("Your answer: ").strip()
    end = time.time()

    time_taken = round(end - start, 2)
    is_correct = user_answer.lower() == q['answer'].lower()

    logging.info(f"Question: '{q['question']}' | Answered in {time_taken} seconds | Correct: {is_correct}")

    results.append([
        q['question'],
        user_answer,
        q['answer'],
        "Yes" if is_correct else "No",
        time_taken
    ])
    print("✅ Correct!\n" if is_correct else f"❌ Wrong! The correct answer is {q['answer']}\n")

# ------------------ SAVE RESULTS ------------------
csv_file = 'results.csv'
with open(csv_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Question", "Your Answer", "Correct Answer", "Correct?", "Time Taken (s)"])
    writer.writerows(results)

print("📄 Results saved to results.csv")
logging.info("Quiz completed and results saved.")
