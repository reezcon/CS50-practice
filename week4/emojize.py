import emoji

def main():
    text = input("Input: ")
    print(f"Output: {emoji_convert(text)}")

def emoji_convert(text):
    return emoji.emojize(text, language="alias")

main()


