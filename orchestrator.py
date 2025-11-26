from learning_agent import LearningAgent
from habit_agent import HabitAgent
from recommend_agent import RecommendationAgent
from content_agent import ContentAgent

class Orchestrator:
    def __init__(self):
        self.learning = LearningAgent()
        self.habit = HabitAgent()
        self.recommend = RecommendationAgent()
        self.content = ContentAgent()

    def handle(self, user_input):
        text = user_input.lower()

        # Learning queries
        if "explain" in text or "what is" in text:
            return self.learning.explain_topic(text)

        # Habit scoring
        elif "i did" in text or "today i" in text:
            score = self.habit.score_habits(text)
            tips = self.recommend.give_recommendations(score)
            return f"Eco Score: {score}\nSuggestion: {tips}"

        # Ask for tips
        elif "tip" in text or "advice" in text:
            return self.recommend.general_tip()

        # Poster / education content
        elif "poster" in text or "message" in text:
            return self.content.make_poster(text)

        else:
            return "I can explain topics, score your habits, or create eco posters. Try asking again!"
