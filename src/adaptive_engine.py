class AdaptiveEngine:
    """
    Adaptive Engine that adjusts question difficulty based on performance.
    """

    def __init__(self):
        self.levels = ["Easy", "Medium", "Hard"]

    def get_next_level(self, current_level, direction):
        idx = self.levels.index(current_level)
        new_idx = max(0, min(idx + direction, len(self.levels) - 1))
        return self.levels[new_idx]

    def adjust(self, current_difficulty, accuracy, avg_time=None, streak=0):
        # Increase difficulty
        if accuracy >= 0.8:
            return self.get_next_level(current_difficulty, +1)

        # Decrease difficulty
        if accuracy <= 0.5:
            return self.get_next_level(current_difficulty, -1)

        # If stable performance, keep same
        return current_difficulty
