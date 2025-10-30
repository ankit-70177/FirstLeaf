# vowel_checker.py
# A simple program to check if a letter is a vowel or a consonant.

print("🔤 Vowel or Consonant Checker")

ch = input("Enter a single letter: ").lower()

if ch in ("a", "e", "i", "o", "u"):
    print(f"{ch} is a vowel 🪶")
elif ch.isalpha():
    print(f"{ch} is a consonant 🔠")
else:
    print("❌ Invalid input! Please enter a single alphabet letter.")
