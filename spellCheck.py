from utils import load_wordlist, suggest_corrections

def spell_check():
    wordlist = load_wordlist('wordlist.txt')

    print("Welcome to the Spell Checker!")

    while True:
        user_input = input("Enter a word (or '111' to exit): ").strip().lower()

        if user_input == '111':
            print("Exiting program.")
            break

        if user_input in wordlist:
            print("The spelling is correct.")
        else:
            suggestion = suggest_corrections(user_input, wordlist)

            if suggestion:
                print(f"Did you mean: {suggestion}?")
            else:
                print(f"No close matches found for '{user_input}'.")
                
if __name__ == "__main__":
    spell_check()