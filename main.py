def main():
    file = ("books/frankenstein.txt")
    with open(file) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
    print (f"Words in book: {word_count}")
        

main()