import string

def analyze_text():
    """Prompts the user for text and calculates various statistics."""

    print("--- Simple Text Analyzer ---")
    print("Enter the text you want to analyze (or type 'quit' to exit):")
    
    # Get multi-line input until the user enters an empty line or 'quit'
    text_lines = []
    while True:
        line = input()
        if line.lower() == 'quit' or line == "":
            break
        text_lines.append(line)

    if not text_lines:
        print("No text entered. Exiting.")
        return

    # Combine all lines into a single string
    full_text = " ".join(text_lines)
    
    # 1. Prepare text for counting (remove punctuation, convert to lowercase)
    # Create a translation table to remove all punctuation
    translator = str.maketrans('', '', string.punctuation)
    clean_text = full_text.lower().translate(translator)
    
    # 2. Calculate Words and Unique Words
    # .split() without arguments splits by any whitespace (spaces, newlines, tabs)
    words = clean_text.split() 
    word_count = len(words)
    
    # Use a set to automatically find all unique words
    unique_words = set(words)
    unique_word_count = len(unique_words)
    
    # 3. Calculate Character Count (excluding all whitespace)
    # Remove all spaces and count the remaining characters
    char_count = len(full_text.replace(' ', '').replace('\n', '').replace('\t', ''))

    # --- Display Results ---
    print("\n" + "=" * 30)
    print("ANALYSIS RESULTS")
    print("=" * 30)
    print(f"Total Words:     {word_count}")
    print(f"Unique Words:    {unique_word_count}")
    print(f"Total Characters (no spaces): {char_count}")
    print("=" * 30)
    
if __name__ == "__main__":
    analyze_text()