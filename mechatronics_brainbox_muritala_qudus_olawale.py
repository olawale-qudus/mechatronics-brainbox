import random

student_name = "MURITALA QUDUS OLAWALE"

questions = [
    {
        "question": "What does PLC stand for?",
        "options": [
            "A. Power Logic Circuit",
            "B. Programmable Logic Controller",
            "C. Programming Line Control",
            "D. Process Level Computer"
        ],
        "answer": "B",
        "level": "Easy"
    },
    {
        "question": "Which language is commonly used for AI?",
        "options": [
            "A. Python",
            "B. HTML",
            "C. CSS",
            "D. SQL"
        ],
        "answer": "A",
        "level": "Easy"
    },
    {
        "question": "What is the function of a sensor?",
        "options": [
            "A. Store energy",
            "B. Detect changes",
            "C. Produce sound",
            "D. Display images"
        ],
        "answer": "B",
        "level": "Easy"
    },
    {
        "question": "Which device converts electrical energy to motion?",
        "options": [
            "A. Resistor",
            "B. Capacitor",
            "C. Electric motor",
            "D. Fuse"
        ],
        "answer": "C",
        "level": "Easy"
    },
    {
        "question": "What does CPU mean?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Power Utility",
            "C. Control Program Unit",
            "D. Central Programming Utility"
        ],
        "answer": "A",
        "level": "Medium"
    },
    {
        "question": "Which component stores electrical charge?",
        "options": [
            "A. Diode",
            "B. Capacitor",
            "C. Transistor",
            "D. Switch"
        ],
        "answer": "B",
        "level": "Medium"
    },
    {
        "question": "What is the main function of an actuator?",
        "options": [
            "A. Measure temperature",
            "B. Store information",
            "C. Produce physical movement",
            "D. Calculate voltage"
        ],
        "answer": "C",
        "level": "Medium"
    },
    {
        "question": "Which system combines mechanics and electronics?",
        "options": [
            "A. Hydraulics",
            "B. Mechatronics",
            "C. Thermodynamics",
            "D. Optics"
        ],
        "answer": "B",
        "level": "Medium"
    },
    {
        "question": "What is the unit of electrical resistance?",
        "options": [
            "A. Volt",
            "B. Ampere",
            "C. Ohm",
            "D. Watt"
        ],
        "answer": "C",
        "level": "Hard"
    },
    {
        "question": "Which device controls current in one direction?",
        "options": [
            "A. Diode",
            "B. Motor",
            "C. Relay",
            "D. Transformer"
        ],
        "answer": "A",
        "level": "Hard"
    },
    {
        "question": "What does PWM stand for?",
        "options": [
            "A. Power Wire Management",
            "B. Pulse Width Modulation",
            "C. Programmed Wave Movement",
            "D. Pulse Work Method"
        ],
        "answer": "B",
        "level": "Hard"
    },
    {
        "question": "Which control system uses feedback?",
        "options": [
            "A. Open-loop system",
            "B. Manual system",
            "C. Closed-loop system",
            "D. Mechanical system"
        ],
        "answer": "C",
        "level": "Hard"
    }
]


def display_welcome():
    print("=" * 45)
    print("       MECHATRONICS BRAINBOX")
    print("=" * 45)
    print("Student:", student_name)
    print("Test your knowledge of Mechatronics!")
    print("12 questions | 1 point per correct answer")
    print("Every 3 consecutive correct answers earn a bonus point.")
    print("=" * 45)


def ask_question(question, number):
    print(f"\nQuestion {number}")
    print("Difficulty:", question["level"])
    print(question["question"])

    for option in question["options"]:
        print(option)

    while True:
        choice = input("Enter A, B, C or D: ").strip().upper()

        if choice in ["A", "B", "C", "D"]:
            return choice
        else:
            print("Invalid choice. Please enter A, B, C or D.")


def calculate_grade(percentage):
    if percentage >= 80:
        return "Excellent"
    elif percentage >= 60:
        return "Very Good"
    elif percentage >= 50:
        return "Good"
    elif percentage >= 40:
        return "Pass"
    else:
        return "Needs Improvement"


def run_quiz():
    score = 0
    streak = 0

    random.shuffle(questions)

    for number, question in enumerate(questions, start=1):
        choice = ask_question(question, number)

        if choice == question["answer"]:
            print("Correct! Well done.")
            score += 1
            streak += 1

            if streak == 3:
                print("STREAK BONUS! +1 point")
                score += 1
                streak = 0
        else:
            print("Incorrect!")
            print("Correct answer:", question["answer"])
            streak = 0

    percentage = (score / 16) * 100
    grade = calculate_grade(percentage)

    print("\n" + "=" * 45)
    print("           FINAL RESULTS")
    print("=" * 45)
    print("Student:", student_name)
    print("Total Score:", score, "/ 16")
    print(f"Percentage: {percentage:.2f}%")
    print("Performance:", grade)
    print("=" * 45)
    print("Thank you for using Mechatronics BrainBox!")


display_welcome()
run_quiz()
