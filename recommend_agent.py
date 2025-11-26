class RecommendationAgent:
    def give_recommendations(self, score):
        if score < 0:
            return "Try reducing plastic use and save electricity."
        elif score == 0:
            return "You're neutral today. Try adding one eco-friendly habit!"
        else:
            return "Great! Keep practicing your eco-friendly habits."

    def general_tip(self):
        return "Eco Tip: Carry a reusable bottle and avoid single-use plastic!"
