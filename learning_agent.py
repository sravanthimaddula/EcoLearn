class LearningAgent:
    def explain_topic(self, text):
        topics = {
            "carbon footprint": "Carbon footprint means the total amount of greenhouse gases you produce by your activities.",
            "recycling": "Recycling means converting waste materials into new usable products.",
            "renewable energy": "Renewable energy comes from natural sources like sun, wind, and water."
        }

        for key in topics:
            if key in text:
                return topics[key]

        return "I can explain carbon footprint, recycling, renewable energy, and more!"
