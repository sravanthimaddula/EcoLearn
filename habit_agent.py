class HabitAgent:
    def __init__(self):
        # Simple dictionary for easy scoring
        self.habits = {
            "plastic": -3,
            "ac": -4,
            "car": -2,
            "bike": 3,
            "bus": 4,
            "train": 4,
            "reusable bottle": 3,
            "reusable bag": 3,
            "water waste": -3
        }

    def score_habits(self, text):
        score = 0
        for habit, value in self.habits.items():
            if habit in text:
                score += value
        return score
