import random

class PuzzleGenerator:
    def generate(self, difficulty):
        if difficulty == "Easy":
            a, b = random.randint(1, 10), random.randint(1, 10)
            return f"{a} + {b}", a + b
