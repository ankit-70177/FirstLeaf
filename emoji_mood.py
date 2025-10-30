# emoji_mood.py
# A simple mood-to-emoji program (Hacktoberfest-friendly!)

def get_emoji(mood):
    mood = mood.lower()
    emojis = {
        "happy": "😊",
        "sad": "😢",
        "angry": "😡",
        "tired": "😴",
        "excited": "🤩",
        "bored": "🥱",
        "confused": "😕",
        "love": "❤️",
        "scared": "😨",
        "surprised": "😲"
    }
    return emojis.get(mood, "🤔 (I don’t know that mood yet!)")

def main():
    print("Welcome to Emoji Mood Generator 😄")
    print("Type your mood (e.g., happy, sad, angry) or 'exit' to quit.")
    while True:
        mood = input("Your mood: ")
        if mood.lower() == "exit":
            print("Goodbye! 👋")
            break
        print("Your emoji:", get_emoji(mood))
        print()

if __name__ == "__main__":
    main()
