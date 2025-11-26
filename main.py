from orchestrator import Orchestrator

bot = Orchestrator()

while True:
    user = input("You: ")
    print("EcoLearn:", bot.handle(user))
