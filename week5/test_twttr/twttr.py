
def main():
    text = input("Input: ")
    print(shorten(text))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    shortened_text = [letter for letter in word if letter.lower() not in vowels]
    shortened_text = "".join(shortened_text)
    return shortened_text

if __name__ == "__main__":
    main()
