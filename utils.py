from difflib import get_close_matches

def load_wordlist(file_path):
    """Load the wordlist into a set for quick lookup."""
    try:
        with open(file_path, 'r') as file:
            return set(line.strip().lower() for line in file)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return set()

def suggest_corrections(word, wordlist):
    """Find corrections one edit away."""
    suggestions = get_close_matches(word, wordlist, n=1, cutoff=0.8)
    return suggestions[0] if suggestions else None

def get_suggestions(word, wordlist):
    """Get suggestions based on Levenshtein distance."""
    suggestions = suggest_corrections(word, wordlist)
    return suggestions