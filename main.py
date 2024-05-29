def main():
    file = ("books/frankenstein.txt")
    with open(file) as f:
        text = f.read()
        words = word_count (text)
        letter_count = count_letters (text)
    print (f"---Begin report of {file} ---")
    print (f"Words in book: {words}")
    #print (f"letters in book: {letter_count}")
    letter_list(letter_count)
    print (f"----End report of {file} ----")

def word_count (text):
    words = text.split()
    return len(words)

def count_letters(text):
    lowered_text = text.lower()
    letters_dict = {}
    for element in lowered_text:
        if element.isalpha():
            if element not in letters_dict:
              letters_dict[element] = 1
            else:
                calculator = letters_dict[element]
                calculator= calculator + 1
                letters_dict[element] = calculator
    return letters_dict

def letter_list(letter_count):
    letter_sortted = sorted(letter_count.items(), reverse=True, key=lambda x:x[1])
    for charecter in letter_sortted:
        print (f"The {charecter[0]}, charecter was found {charecter[1]} times")
    pass
main()