def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return (text)

emoticon = input()
print(convert(emoticon))
