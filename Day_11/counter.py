import sys
import re

def analyze_text(paragraph: str) -> None:
    """Calculates and prints character, word, sentence, and space counts."""
    
    # Requirement: Handle empty input gracefully
    if not paragraph or not paragraph.strip():
        print("Input is empty. All counts are 0.")
        return

    # Calculate basic statistics
    char_count = len(paragraph)
    space_count = paragraph.count(' ')
    
    #  Use split() for basic word counting

    word_count = len(paragraph.split())
    
    #  Consider punctuation when counting sentences
   
    sentences = [s for s in re.split(r'[.!?]+', paragraph) if s.strip()]
    sentence_count = len(sentences)
    
    # Edge case: If a string has words but lacks ending punctuation
    if sentence_count == 0 and word_count > 0:
        sentence_count = 1

    # Output Deliverables
    print("\n--- Calculated Statistics ---")
    print(f"Total Characters: {char_count}")
    print(f"Total Words:      {word_count}")
    print(f"Total Sentences:  {sentence_count}")
    print(f"Total Spaces:     {space_count}")

if __name__ == "__main__":
   
    # multi-line paragraphs without the program terminating prematurely.
    print("Enter your paragraph (Press Ctrl+D on Linux/Mac or Ctrl+Z on Windows to submit):")
    try:
        sample_paragraph = sys.stdin.read()
        analyze_text(sample_paragraph)
    except KeyboardInterrupt:
        print("\nProgram terminated.")
