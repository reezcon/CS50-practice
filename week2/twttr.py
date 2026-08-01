vowels = ["a", "e", "i", "o", "u"]
text = input("Input: ")
shortened_text = [letter for letter in text if letter.lower() not in vowels]
shortened_text = "".join(shortened_text)
print(f"Output: {shortened_text}")
