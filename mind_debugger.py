def analyze_thought(thought):
    if "fear" in thought.lower():
        return "⚠️ Fear detected → possible hesitation"
    elif "excited" in thought.lower():
        return "🚀 High motivation detected"
    else:
        return "🤔 Neutral thinking"

user_input = input("Enter your thought: ")
print(analyze_thought(user_input))
