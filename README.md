📘 About the Project

The Adaptive Math Learning System is a lightweight, rule-based engine that adjusts the difficulty of math questions in real-time based on learner performance.

The purpose of the project is to demonstrate:

Personalized learning through dynamic difficulty adjustment

How rule-based adaptive engines operate

A clean, modular architecture suitable for academic or entry-level ML/AI projects

This project is part of an assignment on designing adaptive systems.

🧠 Key Features
✔ Real-time difficulty adjustment

Switches between Easy, Medium, Hard based on performance.

✔ Rule-based adaptive engine

Transparent, predictable, and easy to modify.

✔ Modular architecture

Each component (generator, tracker, engine) is standalone.

✔ Performance tracking

Tracks accuracy and provides session summary.

✔ Fully terminal-based interaction

Simple, clean, and minimal.

📂 Project Structure
math-adaptive-prototype/
│
├── src/
│   ├── main.py                # Runs the adaptive learning loop
│   ├── puzzle_generator.py    # Generates math problems
│   ├── adaptive_engine.py     # Rule-based difficulty adjustment logic
│   └── tracker.py             # Tracks accuracy and performance
│
└── README.md

🔁 System Workflow
┌────────────────────┐
│    User Answers     │
└──────────┬──────────┘
           ▼
┌────────────────────┐
│ PerformanceTracker │──► accuracy()
└──────────┬──────────┘
           ▼
┌────────────────────┐
│  AdaptiveEngine    │──► new difficulty
└──────────┬──────────┘
           ▼
┌────────────────────┐
│ PuzzleGenerator    │──► new question
└──────────┬──────────┘
           ▼
┌────────────────────┐
│  Display Question  │
└────────────────────┘

🎯 Adaptive Logic

The system uses a simple but effective rule-based approach:

Condition	Action
Accuracy ≥ 80%	Increase difficulty
Accuracy ≤ 50%	Decrease difficulty
Otherwise	Keep the same difficulty

This approach is chosen because:

It is transparent and interpretable

It does not require training data

It is ideal for prototypes

It prevents unstable fluctuations

📊 Metrics Tracked
1. Accuracy
accuracy = correct / total


Used as the primary indicator of proficiency.

2. Streak (optional)

Can trigger upgrades if user is consistently correct.

3. Response Time (optional)

May indicate hesitation, confidence, or struggle.

🧪 How to Run
1. Clone the repository
git clone https://github.com/Rohityd25/math-adaptive-prototype.git

2. Navigate to the src folder
cd math-adaptive-prototype/src

3. Run
python main.py

📝 Example Output
Question 1 (Easy)
7 + 5
Answer: 12
Correct!

Question 2 (Easy)
...

Session Finished
Accuracy: 80.0%
Next Recommended Level: Medium

🛠️ Future Enhancements

ML-based difficulty prediction (logistic regression or RL)

Time-based difficulty modeling

Visualization dashboards for progress tracking

Multiple question types (algebra, geometry, word problems)

Student profiling & personalized pathways

🧑‍💻 Tech Stack

Python 3.x

No external libraries required

Terminal-based interaction
