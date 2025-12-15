import random

class PuzzleGenerator:   # FIXED NAME

    def generate(self, difficulty):
        if difficulty == "Easy":
            return self._easy_problem()
        elif difficulty == "Medium":
            return self._medium_problem()
        elif difficulty == "Hard":
            return self._hard_problem()
        else:
            raise ValueError("Unknown difficulty level")

    def _easy_problem(self):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        q = f"{a} + {b}"
        ans = a + b
        return q, ans

    def _medium_problem(self):
        a = random.randint(5, 20)
        b = random.randint(5, 20)
        q = f"{a} × {b}"
        ans = a * b
        return q, ans

    def _hard_problem(self):
        a = random.randint(10, 30)
        b = random.randint(2, 10)
        q = f"{a} ÷ {b} (round to nearest integer)"
        ans = round(a / b)
        return q, ans
