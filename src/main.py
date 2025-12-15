import time
from puzzle_generator import PuzzleGenerator
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

pg = PuzzleGenerator()
tracker = PerformanceTracker()
engine = AdaptiveEngine()

difficulty = "Easy"

for i in range(5):
    q, ans = pg.generate(difficulty)

    print(f"\nQuestion {i+1} ({difficulty})")
    print(q)

    start = time.time()
    user_ans = int(input("Answer: "))
    end = time.time()

    correct = user_ans == ans
    tracker.log(correct)

    print("Correct!" if correct else f"Wrong! Answer: {ans}")

    # Adjust difficulty after each question
    difficulty = engine.adjust(difficulty, tracker.accuracy())

print("\nSession Finished")
print("Accuracy:", tracker.accuracy() * 100, "%")
print("Next Recommended Level:", difficulty)
