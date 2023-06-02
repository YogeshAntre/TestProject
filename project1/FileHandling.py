def count_lines(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return len(lines)

def count_words(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        words = content.split()
    return len(words)

def count_word_occurrences(file_name, word):
    with open(file_name, 'r') as file:
        content = file.read()
        occurrences = content.lower().count(word.lower())
    return occurrences

def reverse_file(file_name):
    with open(file_name, 'r') as file:
        content = file.readlines()
    reversed_content = reversed(content)
    with open('output.txt', 'w') as output_file:
        output_file.write(''.join(reversed_content))

input_file = 'input.txt'

# 1. Count the number of lines in the file
line_count = count_lines(input_file)
print(f"Number of lines: {line_count}")

# 2. Count the number of words in the file
word_count = count_words(input_file)
print(f"Number of words: {word_count}")

# 3. Count the number of occurrences of a specific word
search_word = input("Enter a word to search: ")
occurrences = count_word_occurrences(input_file, search_word)
print(f"Number of occurrences of '{search_word}': {occurrences}")

# 4. Create a new file named "output.txt" with contents in reverse order
reverse_file(input_file)
print("Reversed file content has been written to 'output.txt'")

