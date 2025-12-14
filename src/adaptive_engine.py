class AdaptiveEngine:
    def adjust(self, difficulty, accuracy):
        if accuracy > 0.8:
            return "Medium"
        if accuracy < 0.5:
            return "Easy"
        return difficulty
