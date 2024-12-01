import difflib

# Function to load the wordlist from a file
def load_wordlist(filename):
    with open(filename, 'r') as file:
        return set(word.strip().lower() for word in file.readlines())

# Function to compute Levenshtein distance (edit distance) between two words
def levenshtein_distance(word1, word2):
    if len(word1) < len(word2):
        word1, word2 = word2, word1  # Ensure that word1 is the longer word

    if len(word2) == 0:
        return len(word1)

    previous_row = range(len(word2) + 1)
    for i, c1 in enumerate(word1):
        current_row = [i + 1]
        for j, c2 in enumerate(word2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

# Function to get word suggestions based on Levenshtein distance
def get_suggestions(word, wordlist):
    suggestions = []
    
    for dict_word in wordlist:
        # Compute the Levenshtein distance
        distance = levenshtein_distance(word, dict_word)
        # We will consider a word a valid suggestion if the edit distance is less than or equal to 2
        if distance <= 2:
            suggestions.append((dict_word, distance))
    
    # Sort suggestions by distance (the closer the word, the higher its rank)
    suggestions.sort(key=lambda x: x[1])

    return suggestions

# Function to check if the word is in the wordlist or suggest a correction
def spell_check():
    wordlist = load_wordlist('wordlist.txt')

    print("Welcome to the Advanced Spell Checker!")

    while True:
        user_input = input("Enter a word (or '111' to exit): ").strip().lower()

        if user_input == '111':
            print("Exiting program.")
            break

        if user_input in wordlist:
            print("The spelling is correct.")
        else:
            suggestions = get_suggestions(user_input, wordlist)

            if suggestions:
                print(f"Did you mean: {', '.join([s[0] for s in suggestions])}?")
            else:
                print(f"No close matches found for '{user_input}'.")

if __name__ == "__main__":
    spell_check()
