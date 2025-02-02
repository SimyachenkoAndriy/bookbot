def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    char_count = {}
    for char in text.lower():  # Convert to lowercase to count case-insensitively
        if char.isalpha():  # Consider only alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


def generate_report(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    
    word_count = count_words(file_contents)
    char_counts = count_characters(file_contents)
    
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


if __name__ == "__main__":
    generate_report("books/frankenstein.txt")
