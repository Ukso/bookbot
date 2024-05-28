def main():
    file = ("books/frankenstein.txt")
    with open(file) as f:
        text = f.read()
        words = word_count (text)
        letter_count = count_letters (text)
    print (f"Words in book: {words}")
    print (f"letters in book: {letter_count}")

def word_count (text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowered_text = text.lower()
    letters_dict = {}
    for element in lowered_text:
        if element.isalpha():
            if element not in letters_dict:
              print(element)
              print("false")
              letters_dict[element] = 1
            calculator = letters_dict[element]
            calculator= calculator + 1
            letters_dict[element] = calculator
    return letters_dict

main()